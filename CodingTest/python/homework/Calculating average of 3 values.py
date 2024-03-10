'''3개의 값에 대한 평균 구하기
(88, 93, 95)'''

# 변수 활용
a = 88
b = 93
c = 95

avg = (a + b + c) / 3
print(avg)

# list 활용
nums = [88, 93, 95]
total = 0

for i in nums:
    total += i

avg = total / len(nums)
print(avg)