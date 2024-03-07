'''모음 제거

문제 설명
영어에선 a, e, i, o, u 다섯 가지 알파벳을 모음으로 분류합니다. 
문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return하도록 solution 함수를 완성해주세요.

제한사항
my_string은 소문자와 공백으로 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000

입출력 예
my_string	result
"bus"	"bs"
"nice to meet you"	"nc t mt y"

입출력 예 #1
"bus"에서 모음 u를 제거한 "bs"를 return합니다.

입출력 예 #1
"nice to meet you"에서 모음 i, o, e, u를 모두 제거한 "nc t mt y"를 return합니다.'''

def solution(my_string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in vowels:
        my_string = my_string.replace(i, '')
    return my_string


# my_string = input()
# def solution(my_string):
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     for i in vowels:
#         my_string = my_string.replace(i, ' ')
#     return print(my_string)

# solution(my_string)


'''
def solution(my_string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in vowels:
        return my_string.replace(i, ' ')

이렇게 적었을 때 실행 오류가 났었는데 for문 아래에 retuen을 넣으면 원래 안되는건가 라는 의문을 가졌었다.
return문이 for문 안에 있으면 for문이 첫번째 반복에서 종료되어서 a에 대한 replace만 수행하고 종료되어 e, i, o, u는 수행이 안된다.
모든 모음을 replace되게 하려면 return을 for문 밖에 적어야 한다.
'''

'''
def solution(my_string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for i in vowels:
        my_string = my_string.replace(i, ' ')
    return my_string

이렇게 하였는데도 오류 발생
replace 하였을 때 '' 사이에 공백을 줘버려서 출력값에 공백이 포함되어 오류가 난것이였다.
'''