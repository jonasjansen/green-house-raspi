# Entrypoint for greenhouse control
import time

from device.light import light

light.turn_on()
time.sleep(1)
light.turn_off()
