import random

def computer_random_number():
    random_number = random.randint(1, 100)
    # return random_number  
    # 플레이어가 컴퓨터의 숫자 카운팅 할때 쓰일 변수. 첫 시작은 0부터
    count = 0

    while True:
        # TypeError: '>' not supported between instances of 'str' and 'int' -> 그냥 되어주면 안될까
        # player_input = input('숫자를 입력하세요 : ')
        player_input = input('숫자를 입력하세요 : ')
        
        # input값으로 숫자가 아니라 문자인 경우에 오류출력하는 코드 
        if player_input.isdigit():  
            player_input = int(player_input)    
            count += 1   # 플레이어가 한번 시도할때마다 횟수 +1 

            # 유효범위 벗어날 경우 알림
            if player_input < 1 or player_input > 100:
                print('1~100사이의 숫자를 입력해 주세요.')

            elif player_input < random_number:
                print('업⬆️')
            elif player_input > random_number:
                print('다운⬇️')
            else:
                print('맞았습니다 🎉')
                print(f'축하합니다! {count}번 만에 성공하습니다.') 
                break
        
        else:
            print('############')
            print('숫자로 입력해 주세요 탈출해주세요')
        
# 게임 재시작 여부
# computer_random_number() 문이 while문 밖에 있으면 함수와 게임이 한번만 호출되어 게임이 한번만 실행된다.
# 후에 게임을 다시 시작하고 싶을 경우 프로그램을 재시작 해야 한다.
while True:
        computer_random_number()
        retry = input('다시 하시겠습니까? (y/n) : ')
        if retry != 'y':
            break

'''
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

'''
유효 범위에서 벗어날 경우 뜨는 알림에 '1~100사이의 숫자를 입력해 주세요.'와 업or다운이 같이떴다.
if문을 2개를 사용해서 다 뜨는것이여서 1~100사이의 숫자 입력 문구를 제일 상단인 if에 적어두고 
다른 조건문들을 elif를 이용해서 적어줬다.
'''