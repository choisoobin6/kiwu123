import tkinter as tk
import RPi.GPIO as GPIO

LED_PIN = 18 # BOARD 기준 11번 핀에 해당

GPIO.setmode(GPIO.BCM)  # BCM 모드로 만듦
GPIO.setup(LED_PIN, GPIO.OUT)

led = False

def led_on():  # on/off를 한번에 쓰는 코드
    global led
    # print("LED 켜짐")
    if led:
        lbl_display.config(text="LED 꺼짐")
        GPIO.output(LED_PIN, GPIO.LOW)
        led = False
    else:
        lbl_display.config(text="LED 켜짐")
        GPIO.output(LED_PIN, GPIO.HIGH)
        led = True

win = tk.Tk()  # 윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")  # 가로 세로 화면 크기
 
btn_on_off = tk.Button(win, text="LED ON/OFF", command=led_on)  # 버튼 객체 생성
lbl_display = tk.Label(win, text="LED DISPLAY")  # 라벨 객체 생성

lbl_display.pack()
btn_on_off.pack(fill='x')  # x축 방향으로 버튼의 너비가 늘어남

win.mainloop()


