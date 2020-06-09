#!/usr/bin/env python3

import argparse
import cv2
import numpy as np
import copy

MX = 3700
MN = 4300

def raw_image_to_ocv_image(raw_img):
    img = raw_img -  MN
    img /= (MX - MN)

    return img


WAIT_KEY = 0
DISPLAY = False

device1 = "/dev/video2"
device2 = "/dev/video3"
device3 = "/dev/video4"

print("ok1")
video1 = cv2.VideoCapture(device1)
video2 = cv2.VideoCapture(device2)
video3 = cv2.VideoCapture(device3)

print("ok2")

ret1 = True
while ret1:
    print("ok")

    ret1, frame1 = video1.read()
    # ret2, frame2 = video2.read()
    # ret3, frame3 = video3.read()
    print()

    if ret1:
        cv2.imshow("stream1", frame1)

    cv2.waitKey(0)



