# toddleplayer
toddleplayer is the manual and a bunch of scripts to create an MP3 and Spotify Player controlled through RFID Tags and GPIO Buttons.

## Hardware

Required:

* A [Raspberry Pi](https://www.raspberrypi.org/products/): I'm using a Pi Zero W

* DAC: You can either use a [pHAT DAC 15€](https://shop.pimoroni.com/products/phat-dac)
or a [PCM5102A 3€](https://www.aliexpress.com/item/1Pcs-PCM5102A-DAC-Sound-Card-Board-pHAT-3-5mm-Stereo-Jack-24-Bits-Digital-Audio-Module/32836159429.html?spm=a2g0s.9042311.0.0.27424c4dOmDi8X)

* Any kind of casing: [Wooden Box](http://www.ebay.de/itm/ZWEIERGRUPPE-EINFACHES-HOLZ-HOLZKISTE-TRUNK-OHNE-GRIFFE-FUR-SERVIETTEN/152320770330?hash=item237706811a:g:3lUAAOSw5cNYLHL1)

* A few push buttons: [Push Buttons](https://www.ebay.de/itm/152295745935?_trksid=p2060353.m2749.l2649&ssPageName=STRK%3AMEBIDX%3AIT)

* A Digital Audio Amplifier:  [PAM8403](https://www.aliexpress.com/store/product/MCIGICM-SAMIORE-ROBOT-PAM8403-mini-5V-digital-amplifier-board-with-switch-potentiometer-can-be-USB-powered/506373_32907755464.html)

* Passive Speakers: [Visaton FR 87](https://www.conrad.de/de/34-zoll-breitband-lautsprecher-chassis-visaton-fr-87-15-w-4-1173601.html)

* A [Powerbank](https://www.amazon.de/LERVING-10000mAh-Powerbank-Ladeger%C3%A4t-Technologie/dp/B00Q2M3AAM/ref=cm_cr_arp_d_product_top?ie=UTF8) or some 18650 Li-Ion Cells and a [Power Supply Board](https://www.aliexpress.com/item/5PCS-5V-Step-Up-Power-Supply-Boost-Converter-Module-Lithium-Battery-Charging-Protection-Board-LED-Display/32852290552.html)

* A [USB RFID READER](https://smile.amazon.de/gp/product/B018OYOR3E/ref=oh_aui_detailpage_o03_s00?ie=UTF8&psc=1) and USB OTG cable or a [MFRC-522](https://www.aliexpress.com/store/product/MCIGICM-MFRC-522-RC522-mfrc-522-RFID-RF-IC-card-inductive-module-S50-Fudan-card-key/506373_32905192359.html)

### Wiring

#### PCMA5102A
To wire up the cheaper PCMA5102A breakout board you have to wire like this:

| PCMA | Raspberry     |
|------|---------------|
| VCC  | 5V PIN 2      |
| GND  | GND           |
| FLT  | GND           |
| DMP  | GND           |
| SCL  | GND           |
| BCK  | GPIO18 PIN 12 |
| DIN  | GPIO21 PIN 40 |
| LCK  | GPIO19 Pin 35 |
| FMT  | GND           |

XMT <–> 10k Resistor <–> 3,3V of the PCM5102A board

#### pHAT DAC
If you use the pHAT DAC you have to solder it [pHAT DAC ](https://forums.pimoroni.com/t/phat-header-soldering-the-lazy-way/1690)



## Software
toddleplayer is based on the Pi Musicbox Image: https://github.com/pimusicbox/pimusicbox ,

the music-cards mopidy extension which I altered heavily: https://github.com/fsahli/music-cards ,


### Pi MusicBox
To create this Player you first have to install Pi Musicbox on your local Raspberry.
You can download the latest image frome here: [RC6](https://github.com/pimusicbox/pimusicbox/releases/tag/v0.7.0RC6)

Burn the image to an SD Card with [Etcher](https://etcher.io/)

1. Put the SD-card into your computer. Ignore the format warning when you're on windows. Open the contents of the 'config' folder of SD-Card in your Finder/Explorer.

2. Open settings.ini and add your Wifi network and password to the file
3. Change 	```enable_ssh = true```

4. Set ```output = hifiberry_dac```

### music-cards extension

If you use a USB RFID Reader continue here. If you use the MFRC-522 continue down below with the RC522_music-cards extension.

Next you have to install python evdev.

```
wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb
dpkg -i python-evdev_0.4.1-1_armhf.deb
```

Then you have to download my forked variant of fsahli's music-cards from here:

https://github.com/tschuehly/music-cards

Then run 'python config.py' to select the RFID reader from the inputs.
### RC522_music-cards extension
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
