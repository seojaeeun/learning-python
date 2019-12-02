#배치 관리자는 컨테이너 안에 존재하는 위젯의 크기와 위치를 자동적으로 관리하는 객체이다.

#1번.격자 배치 관리자
from tkinter import*
window =Tk()

b1 = Button(window, text="One")
b2 = Button(window, text="Three")
b3 = Button(window, text="Two")
b4 = Button(window, text="Four")

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=1, column=0)
b4.grid(row=1, column=1)

window.mainloop()

#2번.압축 배치 관리자
from tkinter import*

window = Tk()

Label(window, text="박스 #1", bg="red", fg="white").pack()
Label(window, text="박스 #2", bg="green", fg="black").pack()
Label(window, text="박스 #3", bg="blue", fg="white").pack()

window.mainloop()

#3번. 
from tkinter import*

#i번쨰 버튼을 누를 수 있는지 겁사한다, 누를 수 있으면 x나o를 표시한다.
def checked(i):
   global player
   button = list[i] #리스트에서 i번째 버튼 객체를 가져온다.

   #버튼이 초기항태가 아니면 이미 누른 버튼이므로 아무것도 하지 않고 리턴한다.

   if button["text"] != "      ":
      return
   button["text"] = "   "+ player + "   "
   button["bg"] = "yellow"
   if player =="X":
      player = "O"
      button["bg"] = "yellow"
   else:
      player = "X"
      button["bg"] = "lightgreen"

window = Tk()      #윈도우를 생성
player = "X"      #시작은 플레이어 X이다.
list = []

#9개의 버튼을 생성하여 격자 형태로 윈도우에 배치한다.
for i in range(9):
   b = Button(window, text = "      ", command = lambda k = i: checked(k))
   b.grid(row = i//3, column = i%3)
   list.append(b)

window.mainloop()

#4번. 스톱워치 만들기
import tkinter as tk

def startTimer():
    if(running):       
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10, startTimer)
    

def start():    
    global running    # 오류 타자오류 ruuning -> running
    running = True    # 오류 타자오류 ruuning -> running

def stop():
    global running
    running = False

running = False
window = tk.Tk()

timer = 0

timeText = tk.Label(window, text="0", font=("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text="시작", bg="yellow", command=start)
startButton.pack(fill=tk.BOTH)

stopButton = tk.Button(window, text="중지", bg="yellow", command=stop)
stopButton.pack(fill=tk.BOTH)

startTimer()
window.mainloop()

# 오류 타자오류 ruuning -> running

#4번. 수정
import tkinter as tk

def startTimer():
   if (running):
      global timer
      timer += 1
      timeText.configure(text = str(timer))
   window.after(10,startTimer)

def start():
   global running
   running = True

def stop():
   global running
   running = False

running = False

window = tk.Tk()

timer = 0

timeText = tk.Label(window, text = "0", font = ("Helvetica", 80))
timeText.pack()

startButton = tk.Button(window, text = "시작", bg = "yellow", command = start)
startButton.pack(fill = tk.BOTH)

stopButton = tk.Button(window, text = "중지", bg = "yellow", command = stop)
stopButton.pack(fill = tk.BOTH)

startTimer()

window.mainloop()

#5번. 마우스 이벤트 처리

window = Tk()

def callback(event):
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

#6번. 마우스 이벤트 처리
from tkinter import*
window = Tk()

def key(event):
    print( repr(event.char), "가 눌렸습니다.")

def callback(event):
    frame.focus_set()
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100, height=100)
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

#JSON: XML보다 데이터 용량이 적고 코드로의 전환이 쉽다는 측면에서 XML의 대체제로