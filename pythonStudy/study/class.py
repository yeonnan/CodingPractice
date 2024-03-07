class Monster:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say(self):
        print(f'나는 {self.name} {self.age}')

shark = Monster('상어', 8)
wolf = Monster('늑대', 3)

shark.say()
wolf.say()

# 클래스는 그 자체로 사용할 수 없고, 인스턴스를 만들어서 사용해야한다.
# 클래스는 추상적인것이기 때문. 자동차 설계도를 타고 다닐 수는 없고 실제로 설계도를 바탕으로 만들어진 차를 타고 다님
# Member를 그대로 사용 못하고// class 추상 인스턴스 실제

# 설계도
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def drive(self):
        print(f'부아앙. 차의 이름은 {self.name}, 색상은 {self.color}') 

# 실제 차를 만듦
car = Car(1, 'a')
car.drive()

#
class Cosmetics:
    def __init__(self, name111, kind):
        self.name = name111
        self.kind = kind
    def use(self):
        print(f'{self.kind}인 {self.name}을 사용했습니다.')

skin_m = Cosmetics('모고어', '스킨')
skin_h = Cosmetics('화산스킨', '스킨')

skin_m.use()
skin_h.use()    

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_name(self):
        print(f'이름은 {self.name}이고, {self.age}살이에요.')

dog1 = Dog('나임', 7)
dog2 = Dog('미소', 7)

dog1.say_name()
dog2.say_name()