import random
import keyword

# count를 변수로 사용해도 될까..?
# print(keyword.kwlist)

def computer_random_number():
    random_number = random.randint(1, 100)
    # return random_number  
    # 플레이어가 컴퓨터의 숫자 카운팅 할때 쓰일 변수. 첫 시작은 0부터
    count = 0

    while True:
        # TypeError: '>' not supported between instances of 'str' and 'int' -> 그냥 되어주면 안될까
        # player_input = input('숫자를 입력하세요 : ')
        player_input = int(input('숫자를 입력하세요 : '))
        count += 1   # 플레이어가 한번 시도할때마다 횟수 기록

        if player_input == random_number:
            print('맞았습니다 🎉')
            # 플레이어가 컴퓨터의 숫자를 카운팅 할때마다 +1
            count += 1
            print(f"축하합니다! {count}번 만에 성공하습니다.") 
            break
        elif player_input > random_number:
            print('다운⬇️')
        else:
            print('업⬆️')

computer_random_number()


'''
오류 1
'숫자를 입력하세요' 다음 업 or 다운이 나오고 바로 끝났다.
왜일까 했는데 내가 바보같이 업이나 다운에도 break문을 적어뒀었다. 
성공시 break문 제외하고 다 없애기
'''

'''
바로 끝나는 굴레에서 벗어나오니 이번엔 정답이 맞는데도 ‘업', ‘다운'만 계속해서 나왔다.
이번에는 if player_input == random_number에 random_number를 문자열로 사용했다.
‘random_number’는 문자열인데 int 정수형으로 비교하려고 해서 발생한 오류였다.

if player_input == random_number: 로 바꿔주니 해결 완료!
'''