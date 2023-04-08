# Entrypoint for greenhouse control
import time

from device.light import light

print(light.get_state())

light.turn_on()
print(light.get_state())

time.sleep(1)

light.turn_off()
print(light.get_state())
