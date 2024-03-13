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
        if n <= 2:
            return n
        
        # 첫 번째와 두 번째 단계의 초기값 설정
        first, second = 1, 2
        
        for i in range(3, n+1):
            # 현재 단계에서의 방법의 수는 이전 두 단계의 합
            third = first + second
            # 다음 단계 계산을 위해 값 업데이트
            first, second = second, third
        
        # n번째 단계에서의 방법의 수 반환
        return second

solution = Solution()
result = solution.climb_stairs(3)
print(result)