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
        