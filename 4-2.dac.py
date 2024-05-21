import RPi.GPIO as GPIO
import time

def dac_signal (x):
    binar = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binar))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

max_volt = 3.3
sampling = 2 ** len(dac)

try:
    T = int(input("Enter the period: "))
    t = T / (2 * sampling)
    while True:
        for i in range(256):
            GPIO.output(dac, dac_signal(i))
            time.sleep(t)

        for i in range(255, 0, -1):
            GPIO.output(dac, dac_signal(i))
            time.sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
