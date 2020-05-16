#!/usr/bin/env python 

import subprocess
import optparse
import re

def main():
    options = get_arguements()
    change_mac(options.interface, options.new_mac)
    return_mac_address(options.interface)
def change_mac(interface, macAddress):
    subprocess.call([ "sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", macAddress,])
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
def return_mac_address(interface):
    macresult = subprocess.check_output(["ifconfig", interface])
    print_new_mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", macresult)

    if print_new_mac_result:
        print("Your new MAC Address is " + print_new_mac_result.group(0))
    else:
        print("Error: Could not see MAC Address, did you select the correct interface?")

main()    
