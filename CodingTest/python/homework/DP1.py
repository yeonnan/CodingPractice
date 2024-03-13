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
        fib_array = [0, 1, 2]
        
        def memo_fibonacci_arr(n):
            if n < len(fib_array):
                return fib_array[n]
            else:
                fib = memo_fibonacci_arr(n-1) + memo_fibonacci_arr(n-2)
                fib_array.append(fib)
                return fib
        
        return memo_fibonacci_arr(n)

sol = Solution()
result = sol.climb_stairs(3)
print(result) 