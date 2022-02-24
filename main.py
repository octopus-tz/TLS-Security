import dns.resolver
import os
import subprocess

# Using readlines()
with open("/home/zisis/Downloads/tranco_K52W.csv") as file:
    for item in file:
        #item = "12,crypto.cloudflare.com"
        print(item)
        a,b = item.split(',', 1)
        print(b)
        cmd = '/home/zisis/Desktop/ldns-1.8.1/drill/drill HTTPS '+b
        print("------------")
        proc = subprocess.Popen([cmd, "/etc/services"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        print("program output:", out)
        print("------------")
        
