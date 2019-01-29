#!python3
from netmiko import Netmiko
import getpass
from time import sleep

userName = 'Administrator'
userPass = getpass.getpass()

testIPs =['10.0.0.1', '10.0.0.2', '10.0.0.3']

def simpleConnect(ip):
    node = {
    "host": (ip),
    "username": userName,
    "password": userPass,
    "device_type": "cisco_ios",}

    net_connect = Netmiko(**node)
    print(net_connect.find_prompt())
    net_connect.write_channel("\r")
    sleep(1)
    if '#' not in (net_connect.find_prompt()): # Checking for enable mode
        net_connect.write_channel("en" + "\r")
        net_connect.write_channel(userPass + "\r")
    print(net_connect.read_channel())
    sleep(1)
    print(net_connect.read_channel())
    output = net_connect.send_command('sh inv') # Change me 
    sleep(1)
    print(output)
    sleep(1)
    net_connect.disconnect()

for ip in testIPs:
    simpleConnect(ip)
