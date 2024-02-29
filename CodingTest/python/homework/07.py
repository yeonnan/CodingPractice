"""
문제 4 Range advanced
1부터 15까지 짝수 * 10, 홀수는 그대로 list에 추가 후 출력
"""

a_list = []

for i in range(1, 16):
    if i % 2 == 0:
        a_list.append(i * 10)
    else:
        a_list.append(i)

print(a_list)

# ex1 = [i*10 if i % 2 == 0 else i for i in range(1, 16)]