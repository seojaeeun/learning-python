#0부터 10000까지 짝수 출력

for i in range(0,10001,2):
    print(i,end="")

#range()함수는 start부터 stop-1까지 step의 간격으로 정수들을 생성한다. start와 step이 대괄호로 싸여져 있는데 
#생략할 수 있다는 의미이다. start나 step이 생략되면 start는 0, step은 1로 간주된다.
#for i in range(statr,stop,step)

#터틀을 이용하여 별 그리기
import turtle

star=turtle.Turtle()

for i in range(5):
    star.forward(300)
    star.right(144)

import turtle

polygon=turtle.Turtle()

num_sides= int(input("다각형의 변의 개수를 입력하시오:" ))
side_length= 70
angle = 360.0/num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

#while 조건식
i=0;
while i < 5:
    print("환영합니다")
    i+=1
    if i == 3:
           break

#구구단

i = int(input("구구단을 입력하시오:"))

while i<11:
    print(number,"*",i,"=",number*i)
    i+=1

#배수의 합 계산 프로그램
sum = 0

for i in range(0,101,3): #최종적인 답만 출력할 때는 for문 밖으로 꺼내야 한다.
   sum+=i

print("1부터 100 사이의 모든 3의 배수의 합은", sum, "입니다.")

#보초값(sentinel)
list_a=[]

for i in range(101):
    list_a.append(i)

print(sum(list_a))
