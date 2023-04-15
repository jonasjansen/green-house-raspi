import RPi.GPIO as GPIO
import time

from config_provider import config


class WindowServo:
    def __init__(self):
        self.gpio_pin = config.get_config('GPIO/SERVO/DATA_PIN')
        self.duty_cycle_open = config.get_config('GPIO/SERVO/DUTY_CYCLE_OPEN')
        self.duty_cycle_closed = config.get_config('GPIO/SERVO/DUTY_CYCLE_CLOSED')
        self.state = "closed"

    def get_state(self):
        return self.state

    def open_window(self):
        self.move_servo(self.duty_cycle_open)
        self.state = "open"
        print("open", self.duty_cycle_open)

    def close_window(self):
        self.move_servo(self.duty_cycle_closed)
        self.state = "closed"
        print("closed", self.duty_cycle_closed)

    def move_servo(self, duty_cycle):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

        # Set GPIO as PWM with 50Hz
        p = GPIO.PWM(self.gpio_pin, 50)
        p.start(2.5)

        # Set to wanted duty cycle
        p.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)

        # Hold position and stop
        p.ChangeDutyCycle(0)
        p.stop()
        GPIO.cleanup()


window_servo = WindowServo()
