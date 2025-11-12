from tkinter import *
from gpiozero import LED

led = LED(18) # BOARD 기준 11번 핀에 해당

win = Tk()  # 윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")

led_on = False

def toggle_led():  # on/off를 한번에 쓰는 코드
    global led_on
    # print("LED 켜짐")
    if led_on:
        led.off()
        led_button.config(text="LED 꺼짐")
        led_on = False
    else:
        led.on()
        led_button.config(text="LED 켜짐")
        led_on = True
        
def on_exit():
    led.off()
    win.destroy()
 
led_button = Button(win, text="LED ON", command=toggle_led, height=2, width=10)  # 버튼 객체 생성
led_button.pack(pady=20)

exit_button = Button(win, text="Exit", command=on_exit, height=2, width=10)  # 라벨 객체 생성
exit_button.pack()

win.mainloop()



