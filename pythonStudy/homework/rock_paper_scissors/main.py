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

while True:
    # 사용자 선택
    user = input('가위, 바위, 보 중 하나를 선택하세요 : ')

    # 컴퓨터 선택
    rps = ['가위', '바위', '보']
    computer = random.choice(rps)
    print(f'사용자 : {user}, 컴퓨터 : {computer}')

    if user() == computer():
        print('비겼습니다 😎')
    elif user('가위') == computer('바위') or user('바위') == computer('보') or user('보') == computer('가위'):
        print('졌습니다 😓')
    else:
        print('이겼습니다 🥳')