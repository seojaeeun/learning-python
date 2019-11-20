#패스워드 생성기 sample,string (과제 4번)
#import random

#def genPass():
#    alphabet = "abcdefghijkmnopqrstuvwxyz0123456789"
#    password= ""

#    for i in range(6):
#        index = random.randrange(len(alphabet))
#        password = password + alphabet[index]
#    return password

#print(genPass())
#print(genPass())
#print(genPass())

#큐(queue):스택과 다르게 먼저 들어간 데이터가 먼저 나오는 'Fist in First Out(FIFO)'의 메모리 구조를 가지는 저장체계이다.

#세트는 집합이므로 중복되면 자동으로 요소 제거된다.

#in 연산자
#numbers = {2,1,3}
#if 1 in numbers:
#    print("집한 안에 1이 있습니다")

#numbers = {2,1,3}
#for x in range(3):
#    for x in numbers:
#        print(x, end="")

#항목 접근하기

#딕셔너리: 키와 값이 서로 연결되어 있다.

#deque 모듈: 스택과 큐를 모두 지원하는 모듈

#문자열 비교하기
#a=input("문자를 입력하시오:")
#b=input("문자를 입력하시오:")

#if(a<b):
#    print(a,"가 앞에 있습니다.")
#else:
#    print(b,"가 앞에 있습니다.")

#s = 'Never put off till tomorrow what you can do today.'
#s.split() # 단어들을 스페이스로 분리, 다른 문자로 분리하려면 인수로 전달

           #(예) s = 'Mississippi'
           #     s.split('i')

#s.isalpha() #문자열이 알파벳으로 구성되어 있는지?
#s.isdigit() #문자열이 숫자로 구성되어 있는지?
#s.islower() #공백문자
#s.isupper() #공백문자
#s.isspace() #공백문자
#s.isalnum() #영숫자인지

#startswith(s), endswith(s), find(s), rfind(s), coumt(s) #메소드
#upper(), lower() #모두 대문자나 소문자로 변환
#capitalize() #첫 문자만 대문자로
#replace(s1,s2) #하나의 문자를 다른 문자로 바꿀 때
#strip() #왼쪽, 오르쪽 공백문자 제거(중간은 제거되지 않음)
#istrip(), rstrip() #왼쪽, 오른쪽 공백문자 제거

#문자열의 분리:split() 함수 자주쓰인다

#회문 검사하기
#from operator import eq
#blank = input("문자열을 입력하시오:")
#change_blank=reversed(blank)
#if eq(blank,change_blank):
#   print("회문입니다.")
#else:
#    print("회문이 아닙니다.")

#couter 클래스
class Counter:
    def reset(self):
        self.count =0 #인스틴스 변수
    def increment(self):
        self.count += 1
    def get(self):
        return self.count
#객체 생성
a = Counter()
a.reset()

for i in range(5):
    a.increment()
    print("카운터 a의 값은", a.get())

#워드에 작성해야할 것:파이썬 데이터 구조(리스트, 딕셔너리, 튜플, set), 문자열 함수들, 스택, 큐, 파일 입출력, 객체 지향





        