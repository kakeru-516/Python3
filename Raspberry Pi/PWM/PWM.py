import RPi.GPIO as GPIO
import time
# GPIO4にPWMを1[Hz]で出力するプログラム

GPIO.setmode(GPIO.BCM)

led_pin = 4
GPIO.setup(led_pin, GPIO.OUT)

led1 = GPIO.PWM(led_pin, 5)
led1.start(50)

#GPIO.output(led_pin, 1)

time.sleep(10)

led1.stop()
GPIO.cleanup()