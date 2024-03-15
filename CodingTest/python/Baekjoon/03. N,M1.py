'''
백준 N과M 1
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열'''

'''
def 재귀함수(n):
	if 정답이면 :
		출력 or 저장
		
	else : 정답이 아니면 :
		for 모든 자식 노드에 대해서:
			if 유망하다면(답의 가능성이 있으면) :
				자식노드로이동
				재귀함수(n+1)
				부모노드로 이동
'''

'''

전역변수로 리스트나 배열 만들고 -> num
함수 선언 -> sequence
그 함수내에 두개의 파라미터! -> n,m
if문 사용 후 개수 확인 len써서 선언한 리스트와 m 비교 -> if len(num) == m:
print 해당 친구를 map써서 프린트 리턴 print(map(str, num)) 

else
리턴값을 for 돌려 if 아닌 애들을 뽑아서 append 
재귀써서 파라미터두개 던져주고 → 해당 ㄹㅣ스트 pop
'''

n, m = list(map(int, input().split()))
num = []    # m개의 수열을 저장할 리스트

def sequence(n,m,num):     
    if len(num) == m:   # num의 길이와 m이 같으면 종료
        print(' '.join(map(str, num)))  # 함수를 str? int?/ ' '.join 이거 뭐에 사용된건지
        return

    for i in range(1, n+1):     # 1~n까지 숫자 확인
        if i not in num:     # num안에 i가 없다면 True
            num.append(i)
            sequence(n,m,num)	# 아마 가지치기..?
            num.pop()
					
sequence(n,m,num)

# 아래코드는 들여쓰기 오류라 뜨는데 틀린게 없어도 계속 오류가 난다.
# n, m = list(map(int, input().split()))
# num = []   

# def sequence(n,m,num):     
#     if len(num) == m:  
#         print(' '.join(map(str, num))) 
#         return
        
# 	for i in range(1, n+1):     
#     	if i not in num:     
# 			num.append(i)
# 			sequence(n,m,num)	
# 			num.pop()
					
# sequence(n,m,num)