#from readtest import *
from CardList import CardList
from Reader import Reader
reader = Reader()
cardList = CardList()
choice = False
while True:
		print 'Place the card in the reader '
		card = reader.readCard()

		while(choice == False):
			localOrSpotify=raw_input('Press [S] for Spotify Playlist [L] for local folder').lower()
			print localOrSpotify
			if localOrSpotify in "s":
				print "You chose Spotify"
				plist=raw_input('Specify Spotify URI, CTRL+C to quit')
				choice == True
			elif localOrSpotify in "l":
				print "You chose Local Music"
				plist=raw_input('Specify local folder path like this: file:/music/Card*/, CTRL+C to quit')
				choice == True
			elif localOrSpotify in "q":
				break
			else:
				print "You gave a non valid choice try again"
			print choice
		cardList.addPlaylist(card, plist)
		if localOrSpotify in "q":
			break
print "Exiting"
