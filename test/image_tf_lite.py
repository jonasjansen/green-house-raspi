"""Main script to run the object detection routine."""
import sys

import tflite_runtime.interpreter as tflite
import numpy as np

MODEL = '/home/pi/green-house-control/test/saved_model.tflite'
IMAGE = '/home/pi/green-house-control/test/img_sprout.png'
#IMAGE = '/home/pi/green-house-control/test/img_seed.png'


def detect():
    try:
        pass
    except Exception as e:
        print(e)


if __name__ == '__main__':
    detect()
