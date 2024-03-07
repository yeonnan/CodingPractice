# map
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

def check_adult(person):
    return '성인' if person['age'] >= 20 else '청소년'

result = map(check_adult, people)

# 람다식
result = map(lambda person:('성인' if person['age'] >= 20 else '청소년'), people)
# people을 돌면서 x에 넣는것. person:person과 똑같다.
# lamda person : ('성인' if person['age'] >= 20 else '청소년', people) 과 같은 말이다.
# peopl을 돌면서 person에 넣을건데, 그 person을 가지고 '성인' if person['age'] >= 20 else '청소년' 으로 리턴해라

result = filter(lambda person:person['age'] > 20, people)

print(list(result))