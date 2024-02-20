a = ('귤', '포도', '망고')

# 튜플은 불변형 으로 바꿀 수 없다.
# a[1] = '수박' # 'tuple' object does not support item assignment
print(a)

# 집합은 중복이 제거되면서 나온다.
b = [1,3,4,6,7,2,4,5,6,9]

a_set = set(b)
print(a_set)    # {1, 2, 3, 4, 5, 6, 7, 9}

a = ['귤', '포도', '망고', '딸기']
b = ['포도', '홍시', '사과']

a_set = set(a)
b_set = set(b)

# 교집합
print(a_set & b_set)    # {'포도'}
# 합집합
print(a_set | b_set)    # {'망고', '홍시', '사과', '귤', '딸기', '포도'}
# 차집합
print(a_set -  b_set)   # {'망고', '딸기', '귤'}