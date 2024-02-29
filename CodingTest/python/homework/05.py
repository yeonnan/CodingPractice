"""
문제 2
새로운 리스트에 kia, hyundai를 추가하라.
"""

cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']
a_list = []

for i in range(len(cars)):
    # print(cars[i])
    if cars[i] == 'kia':
        a_list.append(cars[i])

    if cars[i] == 'hyundai':
        a_list.append(cars[i])

print(a_list)