# value 다 더해주세요(sum)

d = {'a': 15, 'b': 634, 'c': 124, 'd': -436, 'e': -235, 'f': 856, 'g': 23, 'h': 523}

answer = sum(d.values())
print(answer)

# 딕셔너리의 밸류 합 구하는 방법
# 1. 반복문을 사용하여 더하기
answer = 0
for i in d.values():
    answer += i
print(answer)

# 2. sum() 함수 사용
answer = sum(d.values())
print(answer)