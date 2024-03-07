# 정수
a = 3   # 오른쪽에 있는 3이 a에 들어갔다. -> a는 3이다.
b = 5

print(a + b)    # 8
print(a - b)    # -2
print(a * b)    # 15
print(a / b)    # 나누기 0.6
print(a // b)   # 몫 0
print(a % b)    # 나머지 3
print(a ** b)   # a의 b제곱 243

# 소수
c = 3.14
print(c)

# 문자열
d = 'abcde'
print(d)    # abcde

# 참/거짓
e = True
print(e)    # True

f = (3 < 2)
print(f)    # False

num = 2
num = num + 3
print(num)  # 5

# 비교연산자
print(4 > 2)    # True 크다
print(4 < 2)    # False 작다
print(3 >= 2)   # True 크거나 같다
print(3 == 5)   # False 같다
print(2 != 4)   # True 같지 않다

# 논리연산자 이용
ex = 4 > 2

print(ex)   # True
print(not ex)   # False

a and b # False and 연산자 모두 참이어야 참
a or b  # True or 연산자 둘 중 하나만 참이어도 참

# 숫자들의 평균 구하기
num1 = 24
num2 = 16 
num3 = 26

print((num1 + num2 + num3) / 3)