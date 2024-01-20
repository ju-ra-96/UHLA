import RPi.GPIO as GPIO
import time


mic1 = 17
buz1 = 22

mic2 = 23
buz2 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(mic1, GPIO.IN)
GPIO.setup(buz1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(mic2, GPIO.IN)
GPIO.setup(buz2, GPIO.OUT, initial=GPIO.LOW)

def detect1(mic):
    print("Sound Detected1")
    GPIO.output(buz1, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buz1, GPIO.LOW)

def detect2(mic):
    print("Sound Detected2")
    GPIO.output(buz2, GPIO.HIGH)
    time.sleep(2)
    GPIO.output(buz2, GPIO.LOW)

GPIO.add_event_detect(mic1, GPIO.RISING, bouncetime=300)
GPIO.add_event_callback(mic1, detect1)
GPIO.add_event_detect(mic2, GPIO.RISING, bouncetime=300)
GPIO.add_event_callback(mic2, detect2)

while True:
    time.sleep(1)
