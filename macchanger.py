#!/usr/bin/env python 

import subprocess

subprocess.call("sudo ifconfig wlan0 down", shell=True)
subprocess.call("sudo macchanger -r wlan0", shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)
subprocess.call("sudo ifconfig | grep ether", shell=True)
