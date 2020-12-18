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

#### PAM8403

Then you wire the L ,G and R Pins of the PCMA to the Input Pins of the PAM. You connect the + and - power pins of the pam8403 directly to the 5V of the Raspberry and GND. Then you connect your speakers to rout/lout + and -.

#### pHAT DAC
If you use the pHAT DAC you have to solder it. You can solder all of them or solder them the  [lazy way. ](https://forums.pimoroni.com/t/phat-header-soldering-the-lazy-way/1690)

#### RC-522

| RC522| Raspberry     |
|------|---------------|
| 3.3V | 3.3V PIN 1    |
| RST  | GPIO25 PIN 22 |
| GND  | GND           |
| MISO | GPIO9 PIN 21  |
| MOSI | GPIO10 PIN19  |
| SCK  | GPIO11 PIN 23 |
| SDA  | GPIO8 PIN 24  |

## Software


### Pi MusicBox
To create this Player you first have to install Pi Musicbox on your local Raspberry.
You can download the latest image frome here: [RC6](https://github.com/pimusicbox/pimusicbox/releases/tag/v0.7.0RC6)

Burn the image to an SD Card with [Etcher](https://etcher.io/)

1. Put the SD-card into your computer. Ignore the format warning when you're on windows. Open the contents of the 'config' folder of SD-Card in your Finder/Explorer.

2. Open settings.ini and add your Wifi network and password to the file
3. Set 	```enable_ssh = true```

4. Set ```output = hifiberry_dac```

5. Set ```resize_once = true```

You can also set your Spotify and Spotify-Web credentials already.

Then you have to put the SD card in the Raspberry and power it up. You can lookup the IP adress on your router.
To test your wiring connect to the toddleplayer in the webbrowser and run a radiostream unter the tab Streams.

To connect to the Raspberry use your favorite ssh client like [PuTTY](https://www.putty.org/).

The standard user is ```root``` and the password is ```musicbox```.

### First Setup
You have to download the required scripts and unpack them from the latest release.
```
cd ../
wget https://github.com/tschuehly/toddleplayer/releases/download/test/toddleplayer.zip
unzip toddleplayer.zip
rm toddleplayer.zip
cd toddleplayer/
```

### music-cards

If you use a USB RFID Reader continue here. If you use the MFRC-522 continue down below with the RC522_music-cards extension.

Next you have to install python evdev.

```
wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb
dpkg -i python-evdev_0.4.1-1_armhf.deb
```

Then you have to configure it.

```
cd music-cards/
python config.py
```
Select the RFID reader from the inputs. Usually by pressing 0.
### RC522_music-cards

```
sudo nano /boot/config.txt
```
Find this line and remove the '#':
```
#dtparam=spi=on
```
Next, install Python 2.7 dev and gcc using:
```
sudo apt-get update
sudo apt-get install python2.7-dev
sudo apt-get install gcc
```
Then download and install the special SPI tool for python with wget.
```
wget https://github.com/lthiery/SPI-Py/archive/master.zip
unzip master.zip
rm master.zip
cd ./SPI-Py-master
```
then install it by

```
sudo python setup.py install
cd ../
```
Next you have to install python-mpd2 from source here

```
wget https://github.com/Mic92/python-mpd2/archive/master.zip

unzip master.zip
rm master.zip
cd ./python-mpd2-master
python setup.py install
```
### musicbox_gpio script



The easiest way to start the script on startup is to append the following lines to the /opt/musicbox/startup.sh. You have to replace /xxxx/ with either /RC522_music-cards/ or /music-cards/

```
nohup python -u /toddleplayer/gpio_control.py &> /toddleplayer/gpio.log &
echo "started gpio_control.py"
sleep 15
python -u /toddleplayer/xxxx/box.py &> /toddleplayer/box.log &
echo "started box.py"

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

### Credit
The toddleplayer is based on the Pi Musicbox Image: https://github.com/pimusicbox/pimusicbox ,

the music-cards mopidy extension which I altered heavily: https://github.com/fsahli/music-cards ,

the RC522_music-cards project:
https://github.com/tschuehly/RC522_music-cards ,
which uses the MFRC522-python library:
https://github.com/mxgxw/MFRC522-python ,

the python-mpd2 library:
https://github.com/Mic92/python-mpd2 .



&#169; Thomas Schühly
