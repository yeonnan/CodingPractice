'''
- 키보드 Backspace 기능 구현
- input_string = ‘123//45/6789///’
    - /를 만나면 앞의 값을 삭제
    - 참고 - 맨앞에 /만나면 어떻게 처리해야 되는지 생각 해보기  /987////65/432//1/
- answer = ‘146’
'''

def backspace_string(input_string):
    stack = []
    for i in input_string:
        if i == '/':
            if stack:      # /를 만나고, stack에 데이터가 있어야지만 pop 실행       # if==/가 트루고, stack에 데이터가 있으면 stack.pop 실행
                stack.pop()
        else:
            stack.append(i)         # /가 없으면 값 추가
    # print(stack)      # ['1', '4', '6']

    return "".join(stack)   # "" : 해당 요소 사이에 무언가를 넣을 때 사용.  공백 없이 하고싶으면 "" 붙이기 

print(backspace_string("123//45/6789///"))
print(backspace_string("/987////65/432//1/"))