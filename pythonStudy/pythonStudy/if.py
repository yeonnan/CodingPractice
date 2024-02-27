'''
if : 조건이 참일 경우에만 실행. 조건이 거짓일 경우 건너뛴다.
elif : else if의 줄인말로 if문의 조건이 거짓이며 자신의 조건이 참일때 실행. 여러개의 조건을 순차적으로 검사하기 위해 사용
else : if, else의 조건이 모두 거짓일 때 실행. 모든 조건을 만족시키지 못한 경우의 처리를 위해 사용
'''

'''
90점 이상 A
80점 이상 B
70점 이상 C
60점 이상 D
60미만 F
'''

score = int(input('시험 점수를 입력해주세요 : '))   
if score > 100 or score <0:
    print('옳은 점수를 입력해주세요.')
else:
    if score >= 97 :    
        print('아쉽네요~')
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    else:
        print("F")

# 각각 독립적인 if문
# 값을 입력받았을 때 각각의 if문이 서로 영향을 주지 않고 개별적으로 작동한다.
# 첫번째 if문이 true이면 아쉽네요 출력
# 두번째 if문도 true이면 a 출력
    
# 첫번째 결과가 true라고 하더라도 두번째 if문은 score가 90이상인가 만을 고려하고 참인지 거짓인지