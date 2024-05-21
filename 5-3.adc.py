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

def adc_sar (dac, comp):
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

def vol (x):
    x = int (x / 256 * 10)
    arr = [0] * 8
    for i in range (x - 1):
        arr[i] = 1
    return arr

gpio.setwarnings (False)
gpio.setmode (gpio.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

gpio.setup (dac, gpio.OUT, initial=gpio.HIGH)
gpio.setup (leds, gpio.OUT, initial=gpio.HIGH)
gpio.setup (troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup (comp, gpio.IN)

try:
    while True:
        x = adc_sar (dac, comp)
        volt = x * 3.3 / 256
        if x:
            gpio.output (leds, vol (x))

finally:
    gpio.output (dac, 0)
    gpio.output (leds, 0)
    gpio.cleanup ()
