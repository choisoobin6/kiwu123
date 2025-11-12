import RPi.GPIO as GPIO
from time import sleep

red_led = 17  # LED02의 코드를 간결하게 해준 코드, GPIO PIN
green_led = 27
GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)

try:
    while True:
        GPIO.output(red_led, 1)
        GPIO.output(green_led, 0)
        sleep(2)
        GPIO.output(red_led, GPIO.LOW)
        GPIO.output(green_led, GPIO.HIGH)
        sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    # GPIO.cleanup()  #GPIO 설정을 초기화 initialize GPIO setting
    GPIO.cleanup()
