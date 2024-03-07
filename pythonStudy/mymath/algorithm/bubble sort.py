# 버블 정렬로 리스트 구현하기
# 이중 for문으로 코드 구현 가능
# i는 -1
# [7, 5, 2, 6, 1, 8, 9, 4]
# for
# 	for

num = [7, 5, 2, 6, 1, 8, 9, 4]  

for i in range(len(num)-1, 0, -1):   # 뒤에서 부터 검사 범위를 알려주는 문장   //  len(num) -1 이 range()의 시작점
    print("i = ", i)
    for j in range(i): # j가 이동을합니다. 네 // 0부터 너가 정해준 경계까지 검사할게. 0~7까지 하고 0~6으로 
        print("j = ", j)
        if num[j] > num[j + 1]:
            num[j], num[j + 1] = num[j + 1], num[j]
    print(num)   

    # len : 글자수 8개. 근데 갯수가 아닌 index로 접근을 해야해서 0번째 부터 시작 -> 그래서 -1!
    # 7번째 부터[4] 0번째 인덱스인 [7]까지 -1씩 범위씩 이동 누가? i가!
    # 0번째 까지 7번째 까지/ 0번째 부터 6번째/  0~5/0~4/0~3/0~2/0~1/ 0  ->> 이친구가 16번 문장
    # -1, 0, -1   => -1번째인 4부터 시작해서 9 8 1 순으로 가서 7에서 마무리 하겠다.

