# toddleplayer
This is the manual to create an MP3 and Spotify Player controlled through RFID Tags and GPIO Buttons. 
##Hardware

## Software
This is based on the Pi Musicbox: https://github.com/pimusicbox/pimusicbox ,
the music-cards mopidy extension: https://github.com/fsahli/music-cards ,
and the mopidy-ttsgpio extension: https://github.com/9and3r/mopidy-ttsgpio

### Pi MusicBox
To create this Player you first have to install Pi Musicbox on your local Raspberry. 
You can download the Image frome here: https://github.com/pimusicbox/pimusicbox/releases/tag/v0.7.0rc5
The Installation Steps are found on the offical website of Pi MusicBox: http://www.pimusicbox.com/

### mopidy-ttsgpio

You can install the extension by running 
```
pip install Mopidy-TtsGpio
```
Then you have to add the configuration  the MusicBox setting.ini file found in /boot/config/.
```
[ttsgpio]
debug_gpio_simulate = false # Set true to emulate GPIO buttons with on screen buttons
pin_button_main = 17
pin_button_next = 22
pin_button_previous = 23
pin_button_vol_up = 24
pin_button_vol_down = 25
pin_play_led = 27
```

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

https://github.com/Thaiminater/music-cards

Then run 'python config.py' to select the reader from the inputs.
