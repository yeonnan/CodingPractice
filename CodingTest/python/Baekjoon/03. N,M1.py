'''
백준 N과M 1
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
'''

n, m = list(map(int, input().split()))
num = []   

def sequence(n,m,num):     
    if len(num) == m:  
        print(' '.join(map(str, num))) 	
        return

    for i in range(1, n+1):   
        if i not in num:    
            num.append(i)
            sequence(n,m,num)	
            num.pop()
					
sequence(n,m,num)