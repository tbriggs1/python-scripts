#!/usr/bin/env python 

import subprocess


interface = (input("Please enter your Wireless interface card (e.g. wlan0): "))
mac_address = (input("Please enter a MAC Address (e.g. \"00:11:22:33:44:55\") : "))

subprocess.call("sudo ifconfig " + interface + " down", shell=True)
subprocess.call("sudo macchanger -m " + mac_address + " " + interface , shell=True)
subprocess.call("sudo ifconfig " + interface + " up", shell=True)
subprocess.call("sudo ifconfig | grep ether", shell=True)
