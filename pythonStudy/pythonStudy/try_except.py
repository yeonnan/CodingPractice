'''
try:
    먼저 실행할 구문
except:
    실패했을 때 실행할 구문
'''

try:
    num = int(input('숫자를 입력하세요 : '))
    if num % 2 == 0:
        print('짝수입니다.')
    else:
        print("홀수 입니다.")
except:
    print("올바른 값을 입력해주세요.")