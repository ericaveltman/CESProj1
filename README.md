# CESProj1

## What You Need 
### Software
- Processing<br />
`curl https://processing.org/download/install-arm.sh | sudo sh`
- Python 3
- Pandas<br />
`sudo apt-get install python3-pandas`
### Hardware
For this project, I used a Raspberry Pi 3B+ with the Freenove 8 RGB Module. To plug in the LED module, I used pin 2 for power (5V), pin 6 for ground and pin 40 (GPIO 21) for the signal.
## How To Run
### Python Script<br />
In order to run the python script on boot, you have to access your rc.local. To edit, you use
`sudo vim /etc/rc.local`
with whatever text editor you please (just replace vim).<br />
Next add the line `sudo python3 /path to file/led.py` to the end of the file. <br />
Mine looked like `sudo python3 /home/pi/Documents/proj1/led.py`
### Processing<br />
In order to run Processing on boot, you have to access your autostart file. To edit, you use
`sudo vim /etc/xdg/lxsession/LXDE-pi/autostart`<br />
Next add the line `/usr/local/bin/processing-java --sketch=/path to folder/proj1 --run` to the end of the file.<br />
Mine looked like `/usr/local/bin/processing-java --sketch=/home/pi/sketchbook/proj1 --run`<br />
**Note:** For me this only worked with the Processing file in the sketchbook directory and with the file path directing to the folder where the actual file is in
