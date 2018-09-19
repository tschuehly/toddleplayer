This project let's you use a RFID USB Reader to scan RFID tags and play local folders or spotify playlist using pimusicbox or any other mpd server.
I use this USB reader https://www.amazon.de/Neuftech-Reader-Kartenleseger%C3%A4t-Kartenleser-Kontaktlos/dp/B018OYOR3E/


Requires:
- python evdev. To install:
```
wget http://dl.piwall.co.uk/python-evdev_0.4.1-1_armhf.deb
dpkg -i python-evdev_0.4.1-1_armhf.deb
```

- python mpd-2. To install
```
pip install python-mpd2
```
First run 'python config.py' to select the reader from the inputs.
