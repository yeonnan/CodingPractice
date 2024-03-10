'''
배열/연결리스트 문제
- 합격자 수 구하기
- 합격 컷트 라인은 60점
- 점수 : [80, 40, 90, 55, 94, 30, 60, 44]
- answer = 합격자 수(4)
'''

def count_passer(score, c): # score안에서 c이상의 점수 받는 사람
    answer = 0  # c이상의 점수를 받은 사람 카운팅
    for i in score:
        if i >= c:
            answer += 1
    return answer


# [80, 40, 90, 55, 94, 30, 60, 44]
print(count_passer([80, 40, 90, 55, 94, 30, 60, 44], 60))
print(count_passer([20, 50, 20, 80, 45], 30))