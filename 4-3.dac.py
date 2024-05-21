import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

p = GPIO.PWM(19, 1000)

max_volt = 3.3

try:
    while True:
        duty = int(input("Enter the duty cycle: "))
        p.start(duty)
        print("{:.4f}".format(duty * max_volt / 100))
        quit = input("Press q to stop: ")
        p.stop()
        if quit == "q":
            break

finally:
    GPIO.output(19, 0)
    GPIO.cleanup()
