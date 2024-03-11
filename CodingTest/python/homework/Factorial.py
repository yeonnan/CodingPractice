'''
n(팩토리얼)구하기
만약에 n = 5인 경우
출력 값 120
n = 6인 경우
출력 값 720
'''

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))