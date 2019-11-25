#파일에러(경로 다 써야한다) 과제2번

#fname = input("파일 이름:")
#file = open(fname,"r")

#table = dict()
#for line in file:
#    words = line





#객체지향 3요소:캡슐화, 상속, 다형성
#class 안에는 필드와 기능이 들어가 있어야함
#캡슐화 = 필드 + 기능 (안에 들어있는 정보를 알 수 없기 때문에 -> 정보은닉 기능)
#다형성: 모습이 같은게 여러 개 있어도 된다. 변수가 같은게 있어도 된다.
#overriding(오버라이딩): 가까운게 사용된다.
#모든 클래스의 맨 위에는 object 클래스가 있다고 생각하면 된다.

#counter 클래스
#class Counter:
#    def reset(self):
#        self.count = 0  #인스턴스 변수
#    def increment(self):
#        self.count += 1
#    def get(self):
#        return self.count
#객체 생성
#a = Counter()

#a.reset()
#for i in range(5):
#    a.increment()   
#    print("카운터 a의 값은", a.get())

#생성자의 예
#
#class Counter:
#    def __init__(self):
#        self.count = 0
#    def reset(self):
#        self.count = 0

#class Television:
#    def __innit(self, channel, volume, on):
#        self.channel = channel
#        self.volume = volume
#        self.on = on

#    def show(self):
#        print(self.channel, self.volume, self.on)
#    def setChannel(self, channel):
#        self.channel = channel
#    def getChannel(self):
#        return self.channel

###
#class Student:
#    def __init__(self, name=None, age=0):
#        self.__name = name
#        self.__age =age

#    def getAge(self):
#        return self.__age

#    def getName(self):  #name에 대한 접근자
#        return self.__name
    
#    def setAge(self,age):
#        self.__age=age

#    def setName(self, name):   #name에 대한 설정자
#        self.__name=name

#obj=Student("Hong",20)
#obj.getName()
#print(obj.getName())

#obj.setAge(30)
#print(obj.getAge())

#class Vector2D:
#    def __init__(self, x, y):
#        self.x = x
#        self.y=  y

#    def __add__(self, other):
#        return Vector2D(self.x + other.x, self.y + other.y)

#    def __sub__(self, other):
#        return Vector2D(self.x - other.x, self.y - other.y)

#    def __eq__(self, other):
#        self.x == other.x and self.y == other.y

#    def __str__(self):
#        return '(%g, %g)' % (self.x, self.y)

#u = Vector2D(0,1)
#v = Vector2D(1,0)
#w = Vector2D(1,1)
#a = u + v
#print(a)

#if (w==a):
#    print("같다")

class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make # 메이커
        self.model = model # 모델
        self.color = color # 자동차의 색상
        self.price = price # 자동차의 가격

    def setMake(self, make): # 설정자 메소드
        self.make = make

    def getMake(self): # 접근자 메소드
        return self.make

    #차량에 대한 정보를 문자열로 요약하여서 반환한다.
    def getDesc(self):
        return"차량 =("+str(self.make)+","+str(self.model)+","+str(self.color)+","+str(self.price)+")"

class Truck(Vehicle):
    def __init__(self,make,model,color,price,payload):
        super().__init__(make,model,color,price)
        self.payload=payload

    def setPayload(self,payload):   #설정자 메소드
        self.payload=payload

    def getPayload(self):           #접근자 메소드
        return self.payload
myTruck=Truck("Tlsla", "Model S", "white", 10000, 2000)
myTruck.setMake("BMW")
myTruck.setPayload(5000)
print(myTruck.getDesc())
print(myTruck.getMake())
print(myTruck.getPayload())

#상속은 다른 클래스를 재사용하는 탁월한 방법이다. 상속을 사용하면 중복된 코드를 줄일수있다.
#is-a 관계, has-a 관계

