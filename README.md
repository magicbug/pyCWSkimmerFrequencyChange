# Python CW Skimmer Frequency Changer

Python script to automatically change CW Skimmer frequency based on a time period using the telnet connection it offers.

## Setup Options

To use `sdriqswitcher.py` you only need to edit a couple of bits of the script these being `callsign = "m3php"` replacing m3php with you're own callsign.

You might also need to change `HOST = "localhost"`  to the ip address of the windows computer if your running the script on another system for example the Raspberry Pi.

The script listens on the default telnet port `7300` if you have told CW Skimmer to use another port you will need to change this.

## Known Bugs

* If CW Skimmer crashes you will need to restart the script as the telnet connection will fail.

## Task List

- [ ] Make the script function even if Telnet connection fails, reconnecting till it does.
- [ ] Read frequency list from array or json input file.
