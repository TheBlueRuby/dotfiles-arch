#!/usr/bin/python

import subprocess

icons = ["󰕾","󰖁"]

#Get current volume status
volume_status = subprocess.run("wpctl get-volume @DEFAULT_AUDIO_SINK@ | sed 's/Volume: //g'",
                                shell = True,
                                capture_output=True).stdout.decode("utf-8")

if "MUTED" not in volume_status:
    print(" " + icons[0] + " {:.0f}% ".format(float((volume_status))*100))
else:
    print(icons[1])