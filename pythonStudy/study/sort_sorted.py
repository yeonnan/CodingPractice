from glob import glob

# sort
# 변수에 담겨있는 list 자체를 정렬
sample_list = [3, 2, 4, 1, 5]
sample_list.sort() # return data 없이 list 자체를 정렬

print(sample_list) # [1, 2, 3, 4, 5]

# sorted
# 정렬된 list를 return 해주기 때문에 변수에 따로 담아줘야 한다.
sample_list = [3, 2, 4, 1, 5]
sorted_list = sorted(sample_list) # 정렬 된 list를 return

print(sorted_list) # [1, 2, 3, 4, 5]

# 잘못된 방법
sample_list = [3, 2, 4, 1, 5]
sorted_list = sample_list.sort() # .sort()의 return data는 None 입니다.

print(sorted_list) # None