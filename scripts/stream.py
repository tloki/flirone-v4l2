#!/usr/bin/env python3

import argparse
import cv2
import numpy as np
import copy

WAIT_KEY = 0
DISPLAY = False

DISPLAY_TEMPERATURE_MAP_MIN_MAX = (15, 45)

PlanckR1 = 16528.178
PlanckB = 1427.5
PlanckF = 1.0
PlanckO = -1307.0
PlanckR2 = 0.012258549
TempReflected = 20.0
Emissivity = 0.95
ABSOLUTE_ZERO = 273.15


def raw2temperature(RAW):
    # mystery correction factor
    RAW *= 4

    # calc amount of radiance of reflected objects ( Emissivity < 1 )

    RAWrefl = PlanckR1 / (PlanckR2 * (np.exp(PlanckB / (TempReflected + 273.15)) - PlanckF)) - PlanckO

    # get displayed object temp max/min
    RAWobj = (RAW - (1 - Emissivity) * RAWrefl) / Emissivity

    # calc object temperature
    return PlanckB / np.log(PlanckR1 / (PlanckR2 * (RAWobj + PlanckO)) + PlanckF) - ABSOLUTE_ZERO


parser = argparse.ArgumentParser()
parser.add_argument("--device_id", type=str, default="/dev/video2", required=False)
parser.add_argument("--output_file", type=str, default=None, required=False)

args = parser.parse_args()
input_device = "/dev/video2"  # args.device_id
output_file = "sample.avi"  # args.output_file

video = cv2.VideoCapture(input_device)

if output_file is not None:
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    video_writer = cv2.VideoWriter('out2.avi', fourcc, 10, (120, 160))

first = True

i = 0

with open("/tmp/output_LucijaL_09_06_2020_14_09_do_14_38.raw", "wb") as f:
    # for j in range(850000):
    while True:
        ret, frame = video.read()

        if not ret:
            continue

        frame = frame[:, :, 0]
        f.write(frame.copy())

        # frame1 = frame[:, ::2]
        # frame2 = frame[:, 1::2] * 256.0
        # new_frame = frame1 + frame2

        # f.write(new_frame.astype(np.uint16))

        # print(new_frame[0, 0])
        #temps = raw2temperature(new_frame.astype(np.float32))

        #print(temps[0, 0])

        # if output_file is not None:
        #     video_writer.write(new_frame.astype(np.uint8))

        i += 1

print("Frames saved", i)
video.release()
video_writer.release()
