# 난수 생성, 임의의 번호 생성 등 랜덤한 동작이 필요할 때 사용
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(numbers) # numbers를 무작위하게 섞기
print(numbers) # [2, 8, 6, 4, 3, 7, 1, 5]

random_number = random.randint(1, 10) # 1 ~ 10 사이의 무작위 번호 생성
print(random_number) # 4