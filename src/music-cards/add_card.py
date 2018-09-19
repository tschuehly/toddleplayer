#from readtest import *
from CardList import CardList
from Reader import Reader
reader = Reader()
cardList = CardList()

while True:
		print 'Place the card in the reader or press CTRL+C to quit'
		card = reader.readCard()
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
