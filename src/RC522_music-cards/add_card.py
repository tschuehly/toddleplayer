#from readtest import *
from CardList import CardList
import RPi.GPIO as GPIO
import MFRC522
from Reader import readCard
import time
cardList = CardList()
MIFAREReader = MFRC522.MFRC522()

while True:
		print 'Place the card in the reader or press CTRL+C to quit'
		card = readCard(MIFAREReader)
		print card
		localOrSpotify=raw_input('Press [S] for Spotify Playlist [L] for local folder').lower()
		if localOrSpotify in "s":
			plist=raw_input('Specify Spotify URI, q to quit')
			if plist=="q":
				break
		if localOrSpotify in "l":
			plist=raw_input('Specify local folder path like this: file:/music/Card*/, q to quit')
			if plist=="q":
				break
		cardList.addPlaylist(card, plist)
print "Exiting"
