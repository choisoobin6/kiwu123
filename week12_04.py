import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24
RED_LED = 12  # 빨간색 LED를 GPIO 12번 핀에 연결
HRESHOLD = 5  # 거리 임계값(cm)

def setup():  7 usages (6 dynamic)
    GPIO.setmode(GPIO.BCM)
    
    # 초음파 센서 핀 설정 
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    # LED 핀 설정
    GPIO.setup(RED_LED, GPIO.OUT)  
    
    # 초기 상태 설
    GPIO.output(TRIG, False)
    GPIO.output(RED_LED, False)
    print("초음파 센서 준비중 .....")
    time.sleep(2)
    
def get_distance():
    # 초음파 발사
    GPIO.output(TRIG, True)
    time.sleep(0.00001)  # 10마이크로세크의 단위
    GPIO.output(TRIG, False)
    # ECHO 핀에 HIGH가 될 때까지 측정
    pulse_start = time.time()
    time_out = pulse_start + 1
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
        if pulse_start > time_out:
            return -1
        
    # ECHO 핀에 LOW가 될 때까지 측정
    pulse_end = time.time()
    time_out = pulse_end + 1
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
        if pulse_end > time_out:
            return -1
        
    # 시간차 계산
    pulse_duration = pulse_end - pulse_start
    
    # 거리 계산 (음속 34300cm/s)
    distance = pulse_duration * 34300/2
    return round(distance, 2)

def cleanup():
    GPIO.cleanup()
    print("GPIO 자원 회수 완료")
    
if __name__ == "__main__":
    try:
        setup()
        
        while True:
            d = get_distance()
            if d == -1:
                print("측정 오류 : 신호를 받지 못함")
            else:
                print(f"거리 : {d}cm")
            time.sleep(1)
    except KeyboardInterrupt:
        print("프로그램 종료")
    finally:
        cleanup()
