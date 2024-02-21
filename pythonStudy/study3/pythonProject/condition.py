user_list = ["철수", "영희"]

# if문은 기본적으로 다음에 오는 구문이 true인지 false인지 boolean으로 판단한다.
if "철수" in user_list:
    print("user list에 철수가 있습니다")
else:
    print("user list에 철수가 존재하지 않습니다.")

# if문을 사용하지 않고도 true인지 false인지 결괏값을 받을 수 있다.
print("철수" in user_list)

if True or False:
    print("pass")

####

# 스트링 안이나 리스트 안에 내용이 담겨 있을 경우에는 분기문을 통과하지 않는다.
# 내용물이 비어있지 않기 때문에 empty_string, empty_list는 true가 되고, not True는 false이기 때문에 분기문을 통과하지 않는다.
empty_string = ""
empty_list = []

# not은 뒤에 있는 조건이 false 일 때 true가 된다.
if not empty_string:
    print("string is empty!!")

if not empty_list:
    print("list is empty!!")

####

print(bool("")) # False
print(bool(0))  # False
print(bool([])) # False

print(bool("sample"))   # True
print(bool([1, 2]))     # True
print(bool(1))  # True
print(bool(-1)) # 0이 아닌 숫자는 True로 판단
print(bool([""]))   # True 빈 리스트 안의 빈 문자열 / 리스트가 false인 조건은 안에 어떠한 요소도 없을 때이다. 현재는 빈 string이라는 요소가 있어서 결과가 true로 나온다.

###

# all() : 요소들이 모두 True일 경우 True 리턴
if all([True, True, True, False, True]):
    print("통과!") # False가 존재하기 때문에 분기문을 통과하지 못함

# any() : 요소들 중 하나라도 True일 경우 True 리턴
if any([False, False, False, True, False]):
    print("통과!") # True가 1개 이상 존재하기 때문에 분기문을 통과함