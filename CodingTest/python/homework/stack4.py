'''
- 괄호 문법 검사기
- bracket1: [[[[]]]][] → answer ‘YES’
- bracket2: [[[[[[[[[[[[[[[[]] → answer ‘NO’
'''

def is_bracket(b):
    answer = "YES"
    stack = []
    for x in b:
        if x == "]":
            if len(stack) == 0:
                return "NO"
            stack.pop()
        else:
            stack.append(x)

    if len(stack) > 0:
        return "NO"

    return answer


# YES
print(is_bracket("[[[[]]]][]"))

# No
print(is_bracket("[[[[[[[[[[[[[[[[]]"))