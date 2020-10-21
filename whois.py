import sys
import re
import urllib.request

response = urllib.request.urlopen("http://whois.nic.ir/?name=Shokoohi.ir")
for line in response:
    if "no entries found".encode() in line:
        print(line)
    elif "last-updated:".encode() in line:
        print("\nNOT YET")
