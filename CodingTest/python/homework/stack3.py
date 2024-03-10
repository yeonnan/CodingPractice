'''
- N개의 단위로 아래와 같이 리스트로 출력(함수)
- 결과: [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], 
['P', 'Q', 'R'], ['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z']]
'''

alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']

def split_n_list(split_size=3):
    # answer = list()
    answer = []
    
    for i in range(0, len(alphabet_list), split_size):
        # print(i, i+split_size)
        answer.append(alphabet_list[i:i+split_size])
    return answer

print(f"결과: {split_n_list()}")