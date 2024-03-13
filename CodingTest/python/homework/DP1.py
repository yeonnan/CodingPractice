'''
you are climbing a staircase. it  takes n steps to reach the top.
each time you can either climb 1 or 2 steps.
in how many distinct ways can you climb to the top?
1개 또는 2개씩 오르기 가능, 정상에 가려면 n개 올라야함.

- f(1) = 1
- f(2) = 2
'''

class Solution:
    def climb_stairs(self, n: int) -> int:
        # 계단 오르기 문제에서의 초기 조건을 피보나치 수열의 초기값으로 설정
        fib_array = [0, 1, 2]
        
        def memo_fibonacci_arr(n):
            # 이미 계산된 값이면, 바로 반환
            if n < len(fib_array):
                return fib_array[n]
            else:
                # 아직 계산되지 않았다면, 재귀적으로 값을 계산
                fib = memo_fibonacci_arr(n-1) + memo_fibonacci_arr(n-2)
                # 계산된 값을 배열에 추가
                fib_array.append(fib)
                return fib
        
        # n에 대한 계단 오르기 방법의 수를 반환
        return memo_fibonacci_arr(n)

sol = Solution()
result = sol.climb_stairs(3)
print(result) 