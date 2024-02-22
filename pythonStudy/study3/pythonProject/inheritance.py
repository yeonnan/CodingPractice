# class Monster():
#     def __init__(self, hp):
#         self.hp = hp
#
#     def attack(self, damage):
#         self.hp -= damage
#
#     def status_check(self):
#         print(f"monster's hp : {self.hp}")
#
#
# class FireMonster(Monster):
#     def __init__(self, hp):
#         self.attribute = "fire"
#         # super()를 사용하면 부모 클래스의 코드를 그대로 사용할 수 있습니다.
#         # 해당 코드는 self.hp = hp 코드를 실행시키는 것과 동일합니다.
#         super().__init__(hp)
#
#     # 부모 클래스에 존재하는 status_check 메소드를 overriding 합니다.
#     def status_check(self):
#         print(f"fire monster's hp : {self.hp}")
#
#
# class IceMonster(Monster):
#     def __init__(self, hp):
#         self.attribute = "ice"
#         super().__init__(hp)
#
#     def status_check(self):
#         print(f"ice monster's hp : {self.hp}")
#
#
# fire_monster = FireMonster(hp=100)
# # FireMonster 클래스에는 attack 메소드가 없지만
# # 부모 클래스에서 상속받았기 때문에 별도의 선언 없이 사용 가능합니다.
# fire_monster.attack(20)
# fire_monster.status_check()
#
# ice_monster = IceMonster(hp=200)
# ice_monster.attack(50)
# ice_monster.status_check()

class Calc:
    def _print_zero_division_error(self):
        print("can't be division by zero")

    def plus(self, num1, num2):
        ...

    def minus(self, num1, num2):
        ...

    def divide(self, num1, num2):
        if num2 == 0:
            self._print_zero_division_error()
            return False
        ...

    def multiply(self, num1, num2):
        ...


# calc = Calc()
# calc.divide(5, 0)
# # result print
# """
# can't be division by zero
# """

class CustomCalc(Calc):
    def _print_zero_division_error(self):
        print("0으로는 나눌 수 없습니다.")

calc = CustomCalc()
calc.divide(5, 0)
"""
0으로는 나눌 수 없습니다.
"""