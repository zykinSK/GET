import RPi.GPIO as gpio
from time import sleep

def dec2bin (x):
    binar = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binar))

def adc (dac, comp):
    for i in range (256):
        dac_val = dec2bin (i)
        gpio.output (dac, dac_val)
        comp_val = gpio.input (comp)
        sleep (0.01)
        if comp_val:
            return i
    return 0

gpio.setwarnings (False)
gpio.setmode (gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

gpio.setup (dac, gpio.OUT, initial=gpio.HIGH)
gpio.setup (troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup (comp, gpio.IN)

try:
    while True:
        x = adc (dac, comp)
        volt = x * 3.3 / 256
        if x:
            print ("{:.2f}".format (volt))
finally:
    gpio.output (dac, 0)
    gpio.cleanup ()
