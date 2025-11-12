from gpiozero import LED
from time import sleep

red_led = LED(17)  # LED02의 코드를 간결하게 해준 코드, GPIO PIN
green_led = LED(27)

try:
    while True:
        red_led.on()
        green_led.off()
        sleep(2)
        red_led.off()
        green_led.on()
        sleep(2)
except KeyboardInterrupt:
    print("Exit program")
finally:
    # GPIO.cleanup()  #GPIO 설정을 초기화 initialize GPIO setting
    red_led.close() #LED를 꺼줌
    green_led.close()