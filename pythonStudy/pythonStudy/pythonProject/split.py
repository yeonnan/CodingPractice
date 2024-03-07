# split은 string.split("구분자")로 구성되어 있습니다.

string = "hello/python/world!!"
string_list = string.split("/") # split() 안에 들어간 값을 기준으로 문자를 나눈다.

print(string_list) # ['hello', 'python', 'world!!']

# join은 "사이에 들어갈 문자".join(리스트) 로 구성되어 있습니다.

string_list = ["hello", "python", "world"]
string = " ".join(string_list)

print(string) # hello!! python!! world