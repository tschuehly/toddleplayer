# toddleplayer
This is the manual to create an MP3 and Spotify Player controlled through RFID Tags and GPIO Buttons.

## Hardware

Required:

* [Raspberry Pi](https://www.raspberrypi.org/products/): I'm using a Pi Zero W

* USB Soundcard or DAC: I'm using a [pHAT DAC](https://shop.pimoroni.com/products/phat-dac)

* Any kind of casing: I'm using a cheap  [Wooden Box](http://www.ebay.de/itm/ZWEIERGRUPPE-EINFACHES-HOLZ-HOLZKISTE-TRUNK-OHNE-GRIFFE-FUR-SERVIETTEN/152320770330?hash=item237706811a:g:3lUAAOSw5cNYLHL1)

* A few push buttons: I'm using a few cheap [Push Buttons](https://www.ebay.de/itm/152295745935?_trksid=p2060353.m2749.l2649&ssPageName=STRK%3AMEBIDX%3AIT)

* A Digital Audio Amplifier: I'm using a [PAM8403](https://www.ebay.de/itm/PAM8403-Volume-Adjustment-2-Kanal-Digital-Amplifier-Module-Audioverst%C3%A4rker/271513588858?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2060353.m2749.l2649)

* Speakers: I'm using pretty cheap fullrange drivers [Visaton FR 87](https://www.conrad.de/de/34-zoll-breitband-lautsprecher-chassis-visaton-fr-87-15-w-4-1173601.html)

* A Powerbank: I'm using a 10000mAh one [LERVING 10000mAh](https://www.amazon.de/LERVING-10000mAh-Powerbank-Ladeger%C3%A4t-Technologie/dp/B00Q2M3AAM/ref=cm_cr_arp_d_product_top?ie=UTF8)

* A [USB RFID READER](https://smile.amazon.de/gp/product/B018OYOR3E/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1)

### Wiring

#### PCMA5102A
To wire up the cheaper PCMA5102A breakout board you have to wire like this:
* VCC <–> 5V Pin 2
* GND <–> GND
* FLT <–> GND
* DMP <–> GND
* SCL <–> GND
* BCK <–> GPIO18 Pin 12
* DIN <–> GPIO21 Pin 40
* LCK <–> GPIO19 Pin 35
* FMT <–> GND
* XMT <–> 10k Resistor <–> 3,3V of the PCM5102A board

* The first thing you have to do is soldering the pHAT DAC to the Raspberry.
* I soldered all of the pins but you can see how to do it the lazy way here: [pHAT DAC Soldering](https://forums.pimoroni.com/t/phat-header-soldering-the-lazy-way/1690)
* Connect the Powerbank to the Raspberry and to the audio amplifier
* Connect the Speakers to the amplifier and connect the 3.5mm Audio Jack to the amplifier
* Connect up to 5 pushbuttons to the Raspberry: GPIO -- Button -- GND


Here is the wiring of the toddleplayer:
![alt text](https://raw.githubusercontent.com/tschuehly/toddleplayer/master/toddleplayer_wiring.JPG "toddleplayer wiring")

## Software
This is based on the Pi Musicbox: https://github.com/pimusicbox/pimusicbox ,

the music-cards mopidy extension: https://github.com/fsahli/music-cards ,

and my musicbox_gpio script : https://github.com/tschuehly/musicbox_gpio

### Pi MusicBox
To create this Player you first have to install Pi Musicbox on your local Raspberry.
You can download the Image frome here: https://github.com/pimusicbox/pimusicbox/releases/tag/v0.7.0rc5
The Installation Steps are found on the offical website of Pi MusicBox: http://www.pimusicbox.com/

### music-cards extension
Next you have to install python evdev.
```
wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb
dpkg -i python-evdev_0.4.1-1_armhf.deb
```
Then you have to install Python MPD2
```
pip install python-mpd2
```
Then you have to download my forked variant of fsahli's music-cards from here:

https://github.com/tschuehly/music-cards

Then run 'python config.py' to select the RFID reader from the inputs.

### musicbox_gpio script

The next step is to download my musicbox_gpio python script from here: https://github.com/tschuehly/musicbox_gpio

You also have to configure it. Place it in your desired folder but not /music because this is gonna slow down the booting sequence.

The easiest way to start the script on startup is to append the following lines to the /etc/rc.local.

```
/PATH_TO/start.sh 2>&1 | tee /PATH_TO/start.log
```

then you create one start.sh and start.log in a desired folder and paste this into the start.sh
```
#!/bin/bash
sleep 30
python /PATH_TO/gpio_control.py &
```


### Configuration

Now you can create as many folders as you want in the /music/ folder and add the RFID tags accordingly

```
python add_card.py
```

Now you can choose either if you want to add a local folder by pressing [L] or a spotify playlist by pressing [S]

then you have to type in the folder you want to associate with the RFID Card
```
file:/music/foldername/
```

To quit you just have to press CTRL + C

### Sources
https://blog.sengotta.net/connecting-a-pcm5102a-breakout-board-to-a-raspberry-pi/
&#169; Thomas Schühly
