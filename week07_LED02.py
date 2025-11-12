import RPi.GPIO as GPIO
import time

LED_PIN = 18 # BOARD 기준 11번 핀에 해당
GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT)   # set output 출력핀 설정


try:
    while True:
        GPIO.output(LED_PIN, 1)  # LED를 키게 해줌, GPIO.HIGH를 1로 쓸 수도 있음 
        time.sleep(2)  # delay 2초동안 지연시킴 2sec
        GPIO.output(LED_PIN, GPIO.LOW)  
        time.sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    GPIO.cleanup()  #GPIO 설정을 초기화 initialize GPIO setting
