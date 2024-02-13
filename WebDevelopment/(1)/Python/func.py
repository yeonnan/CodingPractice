# 평균을 구하는 함수를 만들어 보겠습니다

# 파이썬으로 평균 구하는 함수
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

numbers = [1, 2, 3, 4, 5]
print(average(numbers)) # 3.0

def sum(a, b, c):   #요리 할 때 재료 넣어주는 것처럼 
    return a + b + c    #재료로 만든 결과물 (요리)

result = sum(1, 2, 3)
print(result)