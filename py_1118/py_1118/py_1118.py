#깊은 복사
scores = [10,20,30,40,50]
values = list(scores)
values[2]=99
print(scores)
print(values)

#리스트와 함수
def func2(list):
    list[0] = 99

value = [0,1,1,2,3,5,8]
print(values)
func2(values)

#함수 함축
list1 =[3,4,5]

# 동적으로2차원 리스트를 생성한다.


# 함수를 작성해보자
# def 함수 이름 (매개 변수 ):
#     수행문 1
#     수행문 2
#     return 반환값

#값을 반환하는 함수  무조건 위에다 써야한다 (인터프리터 이기 때문에)
#def get_sum(start,end):
#    sum=0
#    for i in range(start, end+1):
#        sum+=i
#    return sum
#value = get_sum(1,10)
#print(value)

#함수가 값을 반환
#def get_sum(start,end):
#    sum=0
#    for i in range(start, end+1):
#        sum += i
#    return sum
#value = get_sum(1,10)

#가변 인수
def asterisk_test(a,b,*args):
    return a+b+sum(args)

print(asterisk_test(1,2,3,4,5))

#참조값에 의한 인수 전달(워드에 적기)

#전역 변수를 함수 안에서 사용하려면
def sub():
    global s

    print(s)
    s="바나나가 좋아"

#여러 개의 값 반환하기
def sub():
    return 1,2,3

#무명 함수의 예
sum = lambda x,y: x+y
print("정수의 합:",sum(10,20))
print("정수의 합:",sum(20,40))