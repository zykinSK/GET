import RPi.GPIO as gpio
from time import sleep

def dec2bin (x):
    binar = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binar))

def adc (dac, comp):
    num = 0
    for i in range (7, 1, -1):
        num = num | (1 << i)
        dac_val = dec2bin (num)
        gpio.output (dac, dac_val)
        sleep (0.01)
        comp_val = gpio.input (comp)
        if comp_val == 1:
            num = num & ~(1 << i)
    return num

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
