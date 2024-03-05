# 평균값 구하기

'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
(소수점 첫째 자리에서 반올림한 정수를 출력한다.)

[제약 사항]
각 수는 0 이상 10000 이하의 정수이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''

T = int(input())
for t in range(1, T + 1):
    result = list(map(int, input().split()))
    avg = round(sum(result) / 10)
     
    print(f'#{t} {avg}')

'''
map, int, input, split을 한번에 사용하는것이 어려웠다.
1. input().split()은 사용자로부터 입력받은 문자열을 공백을 기준으로 분리하여 리스트로 만든다.
2. map(int, input().split())는 split() 함수로 분리된 각 문자열을 int() 함수를 통해 정수로 변환한다.
3. list(map(int, input().split()))는 map() 함수의 결과를 실제 리스트로 변환한다.
'''

T = int(input())
num = list(map(int, input().split()))
num.sort()	# 오름차순
division = T//2
result = num[division]

print(result)