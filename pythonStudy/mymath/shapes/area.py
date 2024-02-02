__all__ = ['PI', 'circle']  # area모듈에 import *를 했을 때 PI, circle만 가져오겠다는 뜻
PI = 3.14

# 원의 면적을 구해주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해주는 함수
def square(length):
    return length * length