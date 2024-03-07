people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

# bobby가 age가 없으면 반복문을 돌다가 오류가 난다.
# KeyError: 'age'
# 이럴 때 try-except를 사용하면 실행중에 에러가 난 부분을 넘길 수 있다.
for person in people:
    try:
        if person['age'] > 20:
            print (person['name'])
    except:
        print(person['name'], '에러입니다.')
