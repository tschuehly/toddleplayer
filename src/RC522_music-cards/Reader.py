import RPi.GPIO as GPIO
import MFRC522

def readCard(MIFAREReader):
	while True:
		# Scan for cards
		(status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
		# If a card is found
		if status == MIFAREReader.MI_OK:
			print "Card detected"
			break

	# Get the UID of the card
	(status,uid) = MIFAREReader.MFRC522_Anticoll()
	if uid:
		#print uid
		card = ''.join(str(i) for i in uid)
		return card
