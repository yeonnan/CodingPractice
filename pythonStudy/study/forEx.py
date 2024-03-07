fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)

fruits = ['사과', '배', '감', '귤','귤','수박','참외','감자','배','홍시','참외','오렌지']
for i, fruit in enumerate(fruits):
    print(i, fruit)     # 0 사과 1 배 2 감 3 귤 4 귤
    if i == 4:
        break


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i, name, age)

# 짝수 출력하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
for num in num_list:
    if num % 2 == 0:
        print(num)

# 짝수의 개수 출력하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
count = 0
for num in num_list:
    if num % 2 == 0:
        count += 1
print(count)

# 모든 숫자 더하기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]
sum = 0
for num in num_list:
    sum += num
print(sum)