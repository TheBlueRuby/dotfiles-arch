#!/usr/bin/python

import subprocess

icons = ["󰤨","󰤭"]

#Get current wifi card status
wifi_status = subprocess.run("nmcli -t -f active,ssid dev wifi | grep 'yes' | sed 's/yes://g'",
                                shell = True,
                                capture_output=True).stdout.decode("utf-8").strip() + " "

#if returned string is 0 means there is not any active connection
if wifi_status != "":
    print("" + icons[0])
else:
    print(wifi_status + icons[1])