import RPi.GPIO as GPIO
import time

LED_PIN = 14 # BOARD 기준 11번 핀에 해당
GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT)   # set output 출력핀 설정

while True:
    GPIO.output(LED_PIN, GPIO.HIGH)  # LED를 키게 해줌
    time.sleep(2)  # delay 2초동안 지연시킴 2sec
    GPIO.output(LED_PIN, GPIO.LOW)  
    time.sleep(2)
    
GPIO.cleanup()  #GPIO 설정을 초기화 initialize GPIO setting