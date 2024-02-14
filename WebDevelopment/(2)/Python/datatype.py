# 자료형 : 변수에 들어가는 데이터의 형식 / 숫자, 문자, 리스트, 딕셔너리

name = 'Bob'
hobby = 'python'
print(name + hobby)

num = 12

a_list = ['망고', '귤', '포도', '딸기']
print(a_list[0])        # 망고
a_list.append('체리')
print(a_list)       # ['망고', '귤', '포도', '딸기', '체리']

a_dict = {'name' : '미소', 'age' : 7}
print(a_dict)
print(a_dict['name'])