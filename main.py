#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)


def close():
    # relay = 18
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(relay, GPIO.OUT)
    # GPIO.output(relay, 0)
    print("Door Closed")


def callback(channel):
    if GPIO.input(channel):
        close()


# let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# assign function to GPIO PIN, Run function on change
GPIO.add_event_callback(channel, callback)

# infinite loop
while True:
    time.sleep(1)
