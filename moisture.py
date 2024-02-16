import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
# sensor1 = 22
# sensor2 = 23

def setup_sensor(pin):
    """Setup sensor pin as input."""
    GPIO.setup(pin, GPIO.IN)

def read_moisture(pin):
    """Read and return the moisture level from a specified GPIO pin."""
    print(GPIO.input(pin))
    return GPIO.input(pin)

