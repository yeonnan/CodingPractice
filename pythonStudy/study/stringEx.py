a = '2'
b = str(2)

print(a + b)    # 22

text = 'asdfghjkl'

# 문자열의 길이 세기
result = len(text)
print(result)   # 9

print('@@@@@')
# 문자열 자르기
result = text[:3]   # 처음부터 3번째 까지
print(result)   # asd

# 4번째 문자부터 끝까지
result = text[3:]
print(result)   # fghjkl

result = text[3:7]
print(result)   # fghj

result = text[:]
print(result)   # asdfghjkl

# 문자열 자르기
email = 'abcde@gmail.com'
result = email.split('@')
print(result)

# gma만 출력하기
text = 'gmail'
result = text[:3]
print(result)

# 지역번호만 출력하기
number = '02-1234-5678'
result = number.split('-')[0]
print(result)

ex = 'python StringEx'
print(ex.upper())   # PYTHON STRINGEX
print(ex.lower())   # python stringex

# 슬라이싱
a = 'abcdefghijklmnop'
