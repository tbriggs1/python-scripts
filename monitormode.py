#!/usr/bin/env python

import subprocess

subprocess.call("sudo ifconfig wlan0 down", shell=True)
subprocess.call("sudo iwconfig wlan0 mode monitor", shell=True)
subprocess.call("sudo ifconfig wlan0 up", shell=True)
subprocess.call("sudo iwconfig | grep Mode", shell=True)

