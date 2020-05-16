#!/usr/bin/env python

import subprocess

choice = input("Would you like to put your card into monitor mode or managed mode? - ")
interface = input("Please enter your wireless interface card - ")
def monitor_mode():
    
    subprocess.call("sudo ifconfig " + interface + " down", shell=True)
    subprocess.call("sudo iwconfig " + interface + " mode monitor", shell=True)
    subprocess.call("sudo ifconfig " + interface + " up", shell=True)
    subprocess.call("sudo iwconfig | grep Mode", shell=True)

def managed_mode():

    subprocess.call("sudo ifconfig " + interface + " down", shell=True)
    subprocess.call("sudo iwconfig " + interface + " mode managed", shell=True)
    subprocess.call("sudo ifconfig " + interface + " up", shell=True)
    subprocess.call("sudo iwconfig | grep Mode", shell=True)

if choice == "managed":
    managed_mode()
elif choice == "monitor": 
    monitor_mode()
else:
    print("Please enter managed or monitor")
