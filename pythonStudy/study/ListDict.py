a_list = [1,2,3,4,5,6,7,8,9]
a_list.append(13)   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]

a_list.sort(reverse=True)   # [13, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(a_list)


result = (5 in a_list)
print(result)   # True

a_dict = {'name' : 'bob', 'age' : 27, 'friend' : ['aaa', 'bbb']}

print(a_dict['name'])   # bob
print(a_dict['friend'][1])   # bbb

# 딕셔너리에 값 추가
a_dict['height'] = 180
print(a_dict)   # {'name': 'bob', 'age': 27, 'friend': ['aaa', 'bbb'], 'height': 180}

print('height' in a_dict)   # True

people = [{'name' : 'bob', 'age' : 27}, {'name' : 'John', 'age' : 23}]
print(people[1]['age'])  # 23
###

people = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people[2]['score']['science'])