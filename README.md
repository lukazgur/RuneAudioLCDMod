# RuneAudioLCDMod

RuneAudioLCDMod is a modification of great RuneAudioLCD (https://github.com/RandyCupic/RuneAudioLCD) python script that is used on RuneAudio player for displaying playback information on LCD screen and controlling of player via hardware buttons and IR remote.  

## Modifications
- code migrated to Python 3,
- implementation of direct pins connection for LCD display (I2C is already implemented in original script),
- selection of display screens with hardware button,
- control of backlight ON/OFF with hardware button.

## Requirements
- Raspberry Pi (tested on Pi 2) running RuneAudio (http://www.runeaudio.com/),
- Python 3 installed,
- Adafruit LCD char library installed for parallel display.

## Installation
The easiest solution to run the RuneAudioLCDMod python script every time you turn on RuneAudio player is to setup a deamon
that executes python script. Bash script and service definition are included in repository.
- create a shell script such as /usr/bin/control_script.sh
- create a service file in /lib/systemd/control_script.service
- make systemd aware of your new service:
  - systemctl daemon-reload
  - systemctl enable control_script.service (if error with symbolic link -> run systemctl enable "FULLPATHTOSERVICE")
  - systemctl start control_script.service
- reboot the RPI to see script in action.

#### Useful commands
- systemctl status control_script.service
- systemctl stop control_script.service
- systemctl start control_script.service
- systemctl disable control_script.service

Services "log":
- journalctl /usr/lib/systemd/systemd -b
