# 문제 1. 음수만 더해주세요
# 새로운 리스트에 음수만 더해서 리스트를 출력해주세요
"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할_문장1
    수행할_문장2
"""

ex1_list = [3223, 42, -3, 85, -238, 68, 12]
a_list = []

for i in ex1_list:
    if i < 0:  
        a_list.append(i)  

print(a_list)  