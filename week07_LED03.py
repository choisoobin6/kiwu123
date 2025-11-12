from gpiozero import LED
# import time
from time import sleep

led = LED(17)  # LED02의 코드를 간결하게 해준 코드, GPIO PIN

try:
    while True:
        led.on()
        # time.sleep(2)  # delay 2초동안 지연시킴 2sec
        sleep(2)
        led.off()
        # time.sleep(2)
        sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    # GPIO.cleanup()  #GPIO 설정을 초기화 initialize GPIO setting
    led.close() #LED를 꺼줌

