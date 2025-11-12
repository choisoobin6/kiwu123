# red_led gpio pin 18번 
# 1)LED ON 2)LED OFF 0) QUIT : 1

import RPi.GPIO as GPIO

LED_PIN = 18 # BOARD 기준 11번 핀에 해당

GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT)

def led_on(): # 1 usage
    GPIO.output(LED_PIN, GPIO.HIGH)
    print("LED ON")
    
def led_off(): # 1 usage
    GPIO.output(LED_PIN, GPIO.LOW)
    print("LED OFF")
    
def main(): # 1 usage
    try:
        while True:
            user_input = input("1 LED ON, 2 LED OFF, 0 QUIT: ")
            if user_input == '1':
                led_on()
            elif user_input == '2':
                led_off()
            elif user_input == '0':
                print("프로그램 종료")
                break
            else:
                print("잘못된 입력입니다. 1, 2, 0 중 하나를 입력하세요.")
    except KeyboardInterrupt:
        print("\n프로그램 강제 종료")
    finally:
        GPIO.cleanup()