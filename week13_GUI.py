import tkinter as tk

def led_on():
    # print("LED 켜짐")
    lbl_display.config(text="LED 켜짐")  # 버튼을 누르면 라벨의 내용이 LED 켜짐으로 바뀜
    
def led_off():
    # print("LED 켜짐")
    lbl_display.config(text="LED 꺼짐")  # 버튼을 누르면 라벨의 내용이 LED 켜짐으로 바뀜 

win = tk.Tk()  # 윈도우 객체 생성
win.title("GUI")
win.geometry("400x200")  # 가로 세로 화면 크기
 
btn_on = tk.Button(win, text="LED ON", command=led_on)  # 버튼 객체 생성
btn_off = tk.Button(win, text="LED OFF", command=led_off)  # 버튼 객체 생성
lbl_display = tk.Label(win, text="LED DISPLAY")  # 라벨 객체 생성

lbl_display.pack()
btn_on.pack(fill='x')  # x축 방향으로 버튼의 너비가 늘어남
btn_off.pack(fill='x')

win.mainloop()

# win = tk.Tk()
# win.title("GUI")
# win.geometry("400x200")  # 가로 세로 화면 크기
# win.resizable(False, False)  # 화면 고정
 
# btn_test = tk.Button(win, text="IoT GUI 실습 중...")  # 버튼의 내용이 생성 
# btn_test.pack()  # 버튼이 만들어짐 

# win.mainloop()