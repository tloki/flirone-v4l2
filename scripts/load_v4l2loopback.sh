#!/usr/bin/env bash

# legacy mode:
# sudo modprobe v4l2loopback exclusive_caps=0,0 video_nr=1,2,3

# to run
# git clone https://github.com/umlaeute/v4l2loopback
# cd v4l2loopback
# make
# sudo insmod ./v4l2loopback.ko exclusive_caps=0,0 video_nr=2,3,4

# in my case
# sudo insmod /home/loki/Projects/v4l2loopback/v4l2loopback.ko exclusive_caps=0,0 video_nr=2,3,4

# to run clion or other GUI app as root:
# xhost si:localuser:root
# (run before command)

# to stop:
# sudo modprobe -r v4l2loopback
# sudo depmod -a

# do not install one from Ubuntu repo as it's too old, has a bug:
# https://github.com/umlaeute/v4l2loopback/issues/172

echo "just copy and paste commands commented in this file, do not run directly"