fruits = ['사과', '망고', '배', '귤']

for fruit in fruits:
    print(fruit)

ages = [5, 14, 20, 16, 22, 30]

for age in ages:
    #나이가 20살 보다 크다면
    if age > 20:
        print(f'{age}살은 성인')
    else:
        print(f'{age}살은 청소년')