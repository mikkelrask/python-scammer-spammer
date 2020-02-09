import os

domain = input("URL: ")
ping = "ping -c 1 " + domain + "| awk NR==1{gsub(/\(|\)/,"",$3);print $3}"
iplist = os.popen(ping)
print(iplist)