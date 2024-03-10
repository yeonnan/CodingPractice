'''
[1, 2, 2, 3, 4, 4, 5, 6, 6]에 중복을 제거하라
'''

def remove_duplicates(d_list):
    result = []
    for i in d_list:
        if i not in result:
            result.append(i)
    return result


duplicated_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]

print(remove_duplicates(duplicated_list))