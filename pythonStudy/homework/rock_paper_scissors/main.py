import random

'''
- 플레이어와 컴퓨터의 선택을 비교하여 승패를 판정합니다.
- 결과를 출력하여 플레이어가 이겼는지, 컴퓨터가 이겼는지, 비겼는지를 알려줍니다.
- 게임을 반복하거나 종료할 수 있는 기능을 추가하세요.

게임 계속 반복! 사용자 입력 n을 받을때 까지 -> 반복문
반복문인데 플레이어, 컴퓨터가 가위바위보 선택하는 값 받기
선택값 받으면 받은 값에서 비교
비교한 상태에서 비교를 할때마다 횟수 기록
'''

# # 사용자 선택
# user = input('가위, 바위, 보 중 하나를 선택하세요 : ')

# # 컴퓨터 선택
# rps = ['가위', '바위', '보']
# computer = random.choice(rps)
# print(f'사용자 : {user}, 컴퓨터 : {computer}')

while True:    
    # replay = input('다시 하시겠습니까? (y/n) : ')
    # if replay != 'y':
    #     break 

    # 무한반복이 안되려면 중간에 사용자가 선택한 값이나 컴퓨터가 선택한 값이 바뀌어야 한다.
    # continue가 없으면 if문이 끝난 지점으로 이동, continue가 있으면 다시 반복문으로(28번째줄) 와서 돌기 시작

    # 플레이어나 컴퓨터가 이기거나 질경우 게임 종료
    # 비길경우 게임 계속
    while True:
        # 사용자 선택
        user = input('가위, 바위, 보 중 하나를 선택하세요 : ').upper()   #input.upper(내용)이 아닌 input(내용).upper()
        
        # 컴퓨터 선택
        rps = ['가위', '바위', '보']
        computer = random.choice(rps)
        # computer = '보'
        print(f'사용자 : {user}, 컴퓨터 : {computer}')

        # 게임의 승, 패, 무승부 횟수를 기록. 승/패/비김
        count_win = []
        count_lose = []
        count_tie = []

        if user == computer:
            print('비겼습니다')
            count_tie += 1
            continue
        elif (user == '가위' and computer == '바위') or (user == '바위' and computer == '보') or (user == '보' and computer == '가위'):
            print('졌습니다')
            count_lose += 1
            break
        else:
            print('이겼습니다')
            count_win += 1
            break
        ### continue가 없으면 비겼습니다가 옴

    replay = input('다시 하시겠습니까? (y/n) : ')
    if replay != 'y':
        break

    # if replay == 'n':
    #     print(f'승: {count_win}, 패: {count_lose}, 무승부: {count_tie}')

'''
플레어어나 컴퓨터가 이기거나 질경우 게임 종료, 비길경우 게임 계속 유지
비긴경우에 무한 루프 발생

continue는 for문이면 for로 가서 다시 시작하고, while문이면 while문으로 다시 가서 시작한다.
무한반복이 안되려면 중간에 사용자가 선택한 값이나 컴퓨터가 선택한 값이 바뀌어야 한다.
continue가 없으면 if문이 끝난 지점으로 이동, continue가 있으면 다시 반복문으로 와서 돌기 시작
→ 비길 경우 게임을 다시 시작하고 싶으므로 input값을 while안에 넣어주면 된다.
'''

'''
게임을 다시 시작하는지 선택하는 구문에서 선택에 y를 누르면 계속 물어봄

중첩 while문을 이용하여 게임 한판이 끝난 후 (플레이어가 이기거나 진 후) 유저에게 게임을 계속할것인지 물어본다.
중첩 while문을 사용하여 replay를 제일 아래에 둔 이유는 사용자가 게임을 계속하고 싶을 때마다 게임 전체를 새롭게 시작하게 하려는 의도 때문이다. 
내부 while문은 한판의 게임을 처리하고, break문을 통해 이기거나 진 경우 게임을 종료하고, 비긴경우 continue를 통해 게임을 다시 시작한다.
'''