print(1+1)
print()

print(52, 273, "Hello")
print()

print("안녕하세요", "저의", "이름은", "윤인성입니다!")
print()

print("안녕하세요",'\n',"윤인성입니다!",sep="       ")#띄어쓰기

print("안녕하세요",'\n',"윤인성입니다!",sep="")
print()

print("Hello world")
print()

#굳이 변수를 c언어처럼 선언할 필요가 없다.
a=2
print(a)

a="asdlasdjk"
print(a)

a=1.23456
print(a)

a='a'
print(a)
print()

a= input() #input 문자열로 받는다
print(type(a))
print(a + '1234')
print()

#정수형으로 바꿔주기
a= int( input())
print(a)
print(a + 1234)
print()

print('"안녕하세요" 라고 말했습니다') #따옴표 출력과 같이 출력하기
print("'안녕하세요'라고 말했습니다")

print("\"안녕하세요\"라고 말했습니다")
print('\'배가 고픕니다\'라고 생각했습니다')
print()

print("asdf" * 3)#반복연산자:*
print()

print("안녕하세요"[0]) #문자 선택 연산자(인덱싱):[]
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print()

alp = 'abcdefghijklmnopqrstuvwxyz' #문자열 범위 선택 연산자(슬라이싱): [숫자:숫자]
print(alp[5:11])
print(alp[17:26])
print(alp[-26:-18])
print()

print(len(alp)) #문자열의 길이 구하기
print()

a= 15 #숫자 연산자
b= 8
print("a+b=", a+b)
print("a-b=", a-b)
print("a*b=", a*b)
print("a/b=", a/b) 
print("a%b=", a%b)
print("a//b=", a//b)
print("a**b=", a**b)
print()

print(a+b, a-b, a*b, a/b, a%b, a//b, a**b)
print()

alp = 'abcdefghijklmnopqrstuvwxyz'
tmp=''
for i in alp:
    tmp += i
    print(tmp)
print()

a= input("숫자를 입력하시오: ") #사용자 입력: input()
print()

print(a)