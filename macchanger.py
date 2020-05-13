#!/usr/bin/env python 

import subprocess
import optparse

def change_mac(interface, macAddress):
    
    subprocess.call([ "sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "macchanger", "-m", macAddress, interface])
    subprocess.call(["sudo", "ifconfig", interface, "up"])
def get_arguements():

    parser = optparse.OptionParser() 
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguements) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("Please enter a MacAddress, use --help for more info")
    else:
        return options



options = get_arguements()
change_mac(options.interface, options.new_mac)

