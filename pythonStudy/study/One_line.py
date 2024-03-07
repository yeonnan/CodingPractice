# if
num = 3

# if num % 2 == 0:
#     result = '짝수'
# else:
#     result = '홀수'

result = ('짝수' if num % 2 == 0 else '홀수')

print(f'{num}은 {result}입니다.')


# for
a_list = [1,4,6,7,2,1]

#
b_list = []
for a in a_list:
    b_list.append(a * 2)


# 한줄로 줄여쓰기
# 위의 문장과 아래의 문장은 같은 문장이다.
b_list = [a*2 for a in a_list]   # a_list 안에 있는 a를 돌리는데 그럴때 마다 a * 2를 하고 다 list로 묶어라

print(b_list)