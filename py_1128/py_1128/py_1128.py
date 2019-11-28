# tkinter  ctrl + space:자동완성

# 첫 번째 프로그램
#from tkinter import*

#window = Tk() #루트 윈도우 생성

#label = Label(window, text="Hello World!")
#label.pack() #텍스트를 표시할 정도로만 레이블 위젯의 크기를 축소

#window.mainloop()

## 3*의 뜻은 ***  *:전체, 011 ->01? ?:와일드 카드

##1번
from tkinter import*

window = Tk() 

b1 = Button(window, text="이것이 파이썬 버튼입니다")
b1.pack()

window.mainloop()

#2번
from tkinter import*

window = Tk() 
b1 = Button(window, text="첫번째버튼")
b2 = Button(window, text="두번째버튼")
b1.pack()
b2.pack()

#window.mainloop()

##3번
from tkinter import*

window = Tk() 
b1 = Button(window, text="첫번째버튼")
b2 = Button(window, text="두번째버튼")

b1.pack(side=LEFT)
b2.pack(side=LEFT)

window.mainloop()

#4번
from tkinter import*

window = Tk() 
b1 = Button(window, text="첫번째버튼")
b2 = Button(window, text="두번째버튼")

b1.pack(side=LEFT,padx=10) #왼쪽과 오른쪽에 픽셀을 추가
b2.pack(side=LEFT,padx=10) #pady는 상단과 하단에 픽셀을 추가

window.mainloop()

#5번 버튼의 텍스트 변경
from tkinter import*

window = Tk() 
b1 = Button(window, text="첫번째버튼")
b2 = Button(window, text="두번째버튼")

b1.pack(side=LEFT,padx=10) #왼쪽과 오른쪽에 픽셀을 추가
b2.pack(side=LEFT,padx=10) #pady는 상단과 하단에 픽셀을 추가
b1["text"]="One"
b2["text"]="Two"

window.mainloop()

#6번 버튼의 이벤트를 처리하려면
from tkinter import*

def callback():
    button["text"]="버튼이 클릭되었음!"

window = Tk()
button = Button(window,text="클릭", command=callback)
button.pack(side=LEFT)

window.mainloop()

#7번 클래스로 프레임 감싸기
from tkinter import*

class App:
    def __init__(self):
        window = Tk()
        helloB = Button(window,text="Hello", command =self.hello,fg="red")
        helloB.pack(side=LEFT)
        quitB = Button(window, text="Quit", command=self.quit)
        quitB.pack(side=LEFT)
        window.mainloop()

    def hello(self):
        print("Hello 버튼이 클릭되었음!")

    def quit(self):
        print("Quit 버튼이 클릭되었음!")

App()
 
#8번 색상
from tkinter import*
window = Tk()
button = Button(window, text="버튼을 클릭하세요")
button.pack()
button["fg"]="yellow"
button["bg"]="green"

window.mainloop()

#9번 색상화상자

#from tkinter import*
#color=colorchooser.askcolor()

#10번
from tkinter import*

window = Tk()

w= Label(text = "Helvetica", font= "Helvetica 16")
w.pack()
window.mainloop()

#11번
import tkinter as tk
import tkinter.font as font

class App:
    def __init__(self):
        root=tk.Tk()

        self.customFont = font.Font(family="Helvetica", size=12)

        buttonframe = tk.Frame()
        label = tk.Label(root, text="Hello World!", font=self.customFont)
        buttonframe.pack()
        label.pack()

        bigger = tk.Button(root, text="폰트를 크게", command=self.BigFont)
        smaller = tk.Button(root, text="폰트를 작게", command=self.SmallFont)
        bigger.pack()
        smaller.pack()

        root.mainloop()
    
    def BigFont(self):
        size = self.customFont["size"]
        self.customFont.configure(size=size+2)

    def SmallFont(self):
        size = self.customFont["size"]
        self.customFont.configure(size=size-2)

app=App()

#12번
from tkinter import*

window = Tk()
photo =PhotoImage(file="C:\\Users\\korea\\Desktop\\서영우\\Python\\dog.jpg")
w=Label(window, image=photo)
w.photo = photo
w.pack()
window.mainloop()

#13번 레이블의 색상과 폰트 변경하기
from tkinter import*

window = Tk()

Label(window, text="Times Font 폰트와 빨강색을 사용합니다.", fg="red", font="Times 32 bold italic").pack()

Label(window, text="Helvetica 폰트와 녹색을 사용합니다", fg="blue", bg="yellow", font="Helvetica 32 bold italic").pack()

window.mainloop()

#14번
from tkinter import*

window = Tk()
Label(window, text="이름").grid(row=0)
Label(window, text="나이").grid(row=1)

e1= Entry(window) #빈카을 뚫어줌
e2= Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

window.mainloop()

#15번
from tkinter import*

def show():
    print("이름: %s\n나이: %s" % (e1.get(), e2.get()))

parent = Tk()
Label(parent, text="이름").grid(row=0)
Label(parent, text="나이").grid(row=1)

e1= Entry(parent) #빈카을 뚫어줌
e2= Entry(parent)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(parent, text="보이기", command=show).grid(row=3, column=1, sticky=W, pady=4)
Button(parent, text="종료", command=parent).grid(row=3, column=0, sticky=W, pady=4)

mainloop()

#16번
from tkinter import*

window = Tk()
T = Text(window, height=5, width=60)
T.pack()
T.insert(END, "테스트 위젯은 여러 줄의 \n텍스트를 표시할 수 있습니다.")
mainloop()

#17번 계산기
from tkinter import*
from math import*

def calculate(event):
    label.configure(text = "결과" + str(eval(entry.get())))  #entry.get() 엔트리 값을 받아올때 get사용

window = Tk()

Label(window, text="파이썬 수식 입력:").pack()
entry = Entry(window)
entry.bind("<Return>", calculate)
entry.pack()

label = Label(window, text="결과:")
label.pack()

window.mainloop()

#18번 tkinter을 이용한 그래픽
from tkinter import*

window = Tk()

w=Canvas(window, width=300, height=200)
w.pack()

w.create_rectangle(25,50,200,100)
w.create_line(0,0,300,200)
w.create_line()


#19번 타원 그리기, 호 그리기, 다각형 그리기, 이미지 그리기
from tkinter import*
window = Tk()

canvas= Canvas(window, width=300, height=200)
canvas.pack()

img=PhotoImage(file="주소")
canvas.create_image(20, 20, anchor)

##20번 애니메이션 만들기
import time
from tkinter import*
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()
id=canvas.create_oval(10, 100, 50, 150, fill="#bfaf45")

for i in range(100):
    canvas.move(id, 3, 0) #x,y 방향 이동거리
    window.update()
    time.sleep(0.05)

##21번 화살표를 받아 이동하기
from tkinter import*
window = Tk()
canvas = Canvas(window, width=400, height=300)
canvas.pack()

id = canvas.create_oval(10, 100, 50, 150, fill="green")

def move_right(event):
    canvas.move(id, 5, 0)
canvas.bind_all("<KeyPress-Right>", move_right)

window.mainloop()

#22번 라디오 버튼
from tkinter import *

window =tk()
choice = intvar()

label(window, text = "가장 선호하는 프로그래밍 언어를 선택하시오", justify = left, padx = 20).pack()
radiobutton(window, text = "python", padx = 20, variable = choice, value = 1).pack(anchor =w)#왼쪽에 붙인다.
radiobutton(window, text = "c", padx = 20, variable = choice, value = 2).pack(anchor =w)#왼쪽에 붙인다.
radiobutton(window, text = "java", padx = 20, variable = choice, value = 3).pack(anchor =w)#왼쪽에 붙인다.
radiobutton(window, text = "swift", padx = 20, variable = choice, value = 4).pack(anchor =w)#왼쪽에 붙인다.

window.mainloop()

#23번 리스트 박스
from tkinter import*

window = Tk()

b=Listbox(window.height=4)
b.pack()
b.insert(END,"Python")
b.insert(END,"C")
b.insert(END,"Java")
b.insert(END,"Swift")

window.mainloop()


