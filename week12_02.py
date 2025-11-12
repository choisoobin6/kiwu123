import RPi.GPIO as GPIO
from time import sleep

LED1 = 12
LED2 = 13

GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(LED1, GPIO.OUT)   # set output 출력핀 설정
GPIO.setup(LED2, GPIO.OUT)

pwm1 = GPIO.PWM(LED1, 1000) # 주파수 설정 1kHz == 1000Hz, pwm 객체 생성
pwm2 = GPIO.PWM(LED2, 1000)

pwm1.start(0)  # Duty cycle 0%로 할당
pwm2.start(0)

try:
    while True:
        for dc in range(0, 101, 1):
            pwm1.ChangeDutyCycle(dc)
            sleep(0.02)
        for dc in range(100, -1, -1):
            pwm2.ChangeDutyCycle(dc)
            sleep(0.02)
except KeyboardInterrupt:
    print("프로그램 종료")
finally:
    pwm1.stop()
    pwm2.stop()
    GPIO.cleanup()

