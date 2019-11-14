##동전 주는 프로그램
price = int(input("물건값을 입력하시오: "))

one_thousand =int(input("1000원 지폐개수: "))
five_hundred = int(input("500원 동전개수: "))
one_hundred = int(input("100원 동전개수: "))

price = (1000*one_thousand + 500*five_hundred + 100*one_hundred) - price

thousand = price//1000
price = price%1000
f_hundred = price//500
price = price%500
hund = price//100
price = price%100
ten = price//10
price = price%10

print("1000원:",thousand)
print("500원:",f_hundred)
print("100원:",hund)
print("10원:",ten)

print("나머지:", price)


#swpt
a=10
b=20
c=30
d=40

a,b=c,d
a,b,c,d = d,c,b,a

print(a,b,c,d)

if(a>b):
    print("a가 큽니다.")
else:
    print("b가 a보다 큽니다.")

#tutle
import turtle
t=turtle.Pen()

while True: #무한반복
    direction = input("왼쪽=left, 오른쪽=right:")
    if direction == "l":
        t_left(60)
        t_forward(50)
    if direction == 'r':
        t_right(60)
        t_forward(50)


#홀수 짝수
#count = 0
#while (count < 10):
#    number = int(input("정수를 입력하시오: "))
#   if (number % 2) == 0:
#      print(number,"짝수입니다")
#   else:
#      print(number,"홀수입니다")
#    count += 1

#물건값 계산
total_price= int(input("구입 금액을 입력하시오:"))
if total_sales > 100000:
    print("지불금액은",price - (price*(5/100)), "입니다.")
else:
    print("지불금액은",price,"입니다.")

#졸업 학점 검사하기
score= int(input("이수한 학점수를 입력하시오: "))
grade= float(input("평점을 입력하시오: "))
if score > 140 and grade > 2.0:
    print("졸업할 수 있습니다")
else:
    print("졸업이 힘듭니다!")

#날짜 시간 출력하기
import datetime

now = datetime.datetime.now()

print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now. second, "초")

if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))


    






