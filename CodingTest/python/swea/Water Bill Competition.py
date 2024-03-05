# 수도 요금 경쟁

# A사 : 1리터당 P원의 돈을 내야 한다.

# B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 
#      하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.

# 종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.

# 각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 
# P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.

t = int(input())
for t in range(1, t+1):
     
    P, Q, R, S, W = map(int, input().split())
     
    A = P*W
    B = Q
    if W > R:
        B += (W-R) * S
         
    if A > B:
        print(f'#{t} {B}')
    else:
        print(f'#{t} {A}')