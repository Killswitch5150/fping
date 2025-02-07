#fping is an ironically not easier to use version of ping that is dependent on ping
#it solves zero problems, makes nothing easier, but it does accomplish the same job, and taught me how to accept command line arguments for my programs

#example cli call "python3 fping.py 8.8.8.8 -4"

import argparse  #library used to allow CLI arguments
import os  #used to allow system interaction

# argparse initialization
parser = argparse.ArgumentParser(description="fping is a slightly faster ping script. saving users an average of typing one letter.")  #appears with --help
parser.add_argument('ip_target', type=str, help="Target IP Address to ping")  #argument for IP address
parser.add_argument('-c', '--count', type=int, default=4, help="Number of packets (default is 4)")  #argument for packet count

args = parser.parse_args() #saves cli input to args datatype (list?)

# Access the arguments
ip_target = args.ip_target  #saves the IP target info from the CLI
ping_count = args.count  #saves the packet count from the CLI

print(f"Sending {ping_count} packets to {ip_target}") #print feedback for troubleshooting/confirmation

os.system(f'ping -c {ping_count} {ip_target}') #runs ping command

input("Press any Key to Exit") #placeholder to keep console open when running standalone
