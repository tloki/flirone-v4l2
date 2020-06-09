#!/usr/bin/env bash

# deprecated:
#echo "$LOGIN_PASSWD" | sudo -S yourExecutable palettes/Grayscale.raw

# TODO: enable this as script
# put:
# SUBSYSTEM=="usb", ATTRS{idVendor}=="09CB", ATTRS{idProduct}=="1996", MODE="0666", GROUP="plugdev"
# in
# /etc/udev/rules.d/50-flirone-rule.rules
# udevadm control --reload-rules
# usermod -aG video,plugdev $USER

echo "for now, just follow instructions inside this file, not running this file"
