'''
접두사인지 확인하기

문제 설명
어떤 문자열에 대해서 접두사는 특정 인덱스까지의 문자열을 의미합니다. 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"입니다.
문자열 my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1을, 아니면 0을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ my_string의 길이 ≤ 100
1 ≤ is_prefix의 길이 ≤ 100
my_string과 is_prefix는 영소문자로만 이루어져 있습니다.

입출력 예
my_string	is_prefix	result
"banana"	"ban"	1
"banana"	"nan"	0
"banana"	"abcd"	0
"banana"	"bananan"	0

입출력 예 #1
예제 1번에서 is_prefix가 my_string의 접두사이기 때문에 1을 return 합니다.
입출력 예 #2
예제 2번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.
입출력 예 #3
예제 3번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.
입출력 예 #4
예제 4번에서 is_prefix가 my_string의 접두사가 아니기 때문에 0을 return 합니다.
'''

def solution(my_string, is_prefix):
    if my_string.startswith(is_prefix):
        return 1
    else:
        return 0


# startswith()는 문자열이 특정 문자열 또는 접두사로 시작하는지를 확인. 문자열이 지정된 접두사로 시작하면 True 반환, 아니면 False 반환.