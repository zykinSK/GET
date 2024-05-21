import RPi.GPIO as GPIO

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
    while True:
        number = input("Enter the number from 0 to 255: ")
        try:
            if number == "q":
                break

            number = int(number)
            if 0 <= number <= 255:
                GPIO.output(dac, dac_signal(number))
                volt = max_volt * number / sampling
                print("Voltage = ", "{:.4f}".format(volt))
            else:
                print("Incorrect number")

        except Exception:
            print("Not a number")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
