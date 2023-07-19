#!/bin/bash
grim -g "$(slurp -d)" - | wl-copy -t image/png
