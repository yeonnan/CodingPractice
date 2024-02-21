def func1():
    number = 10  # 함수 내에서 number라는 지역 변수를 선언


def func2():
    print(number)  # func1에서 생성된 지역 변수는 funt2에서 접근할 수 없다.


func1()
func2()

"""
Traceback (most recent call last):
  File "sample.py", line 8, in <module>
    func2()
  File "sample.py", line 5, in function2
    print(number)
NameError: name 'number' is not defined
"""

number = 10  # 함수 밖에서 number라는 전역 변수 생성


def func():
    print(number)  # 전역 변수는 자유롭게 접근할 수 있다.


func()  # 함수를 실행하면 10이 정상적으로 출력된다.