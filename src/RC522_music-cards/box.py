#!/usr/bin/env python
from mpd import MPDClient
import re
from CardList import CardList
import sys
import os
import RPi.GPIO as GPIO
import MFRC522
from Reader import readCard
import time

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()



def connectMPD():
	try:
		client = MPDClient()               # create client object
		client.timeout = 200               # network timeout in seconds (floats allowed), default: None
		client.idletimeout = None
		print "Connecting..."
		client.connect("localhost", 6600)
		print "Connected!"
		return client
	except:
		print 'Could not connect to MPD server'

def playlist(client,plist):
	try:
		plist2 = re.sub('file:','',plist)
		print plist
		for root,dirs,files in os.walk(plist2):
			for filename in files:
				filename = plist + filename
				print filename
				client.add(filename)
		return plist
	except Exception as e:
		print(e)

def play(client, plist):
	try:
		client.stop()
		client.clear()
		if re.search('file', plist):
			playlist(client,plist)
			client.shuffle()
		if re.search('spotify',plist):
			client.add(plist)
			client.shuffle()
		client.play()
	except:
		print 'Could not play playlist %s' % plist


MIFAREReader = MFRC522.MFRC522()
cardList = CardList()

print 'Ready: place a card on top of the reader'

while True:
	try:
		card = readCard(MIFAREReader)
		print 'Read card', card

		plist = cardList.getPlaylist(card)
		if plist != '':
			print 'Playlist', plist
			client = connectMPD()
			if plist=='pause':
				client.pause()
			else:
				play(client, plist)
			client.close()
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
		sys.exit(0)
	except:
		pass
