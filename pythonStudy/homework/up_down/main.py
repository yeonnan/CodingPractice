import random
import keyword

print(keyword.kwlist)

def computer_random_number():
    random_number = random.randint(1, 100)
    # 플레이어가 컴퓨터의 숫자 카운팅 할때 쓰일 변수. 첫 시작은 0부터
    count = 0
    # return random_number

    while True:
        # TypeError: '>' not supported between instances of 'str' and 'int' -> 그냥 되어주면 안될까
        # player_input = input('숫자를 입력하세요 : ')
        player_input = int(input('숫자를 입력하세요 : '))
        print()
        if player_input == 'random_number':
            print('맞았습니다 🎉')
            # 플레이어가 컴퓨터의 숫자를 카운팅 할때마다 +1
            count += 1
            break
        elif player_input > random_number:
            print('다운')
            break
        else:
            print('업')
            break

computer_random_number()
# print(keyword.kwlist)