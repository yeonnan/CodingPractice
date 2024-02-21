number = "num"

try: # try 구문 안에서 에러가 발생할 경우 except로 넘어감
    number = int(number) # "num"을 숫자로 바꾸는 과정에서 에러 발생
except: # 에러가 발생했을 때 처리
    print(f"{number}은(는) 숫자가 아닙니다.")

number = input()

try:
    int(number)
    10 / number

except ValueError:  # int로 변환하는 과정에서 에러가 발생했을 떄
    print(f"{number}은(는) 숫자가 아닙니다.")

except ZeroDivisionError:  # 0으로 나누면서 에러가 발생했을 때
    print("0으로는 나눌수 없습니다.")

except Exception as e:  # 위에서 정의하지 않은 에러가 발생했을 때(권장하지 않음)
    print(f"예상하지 못한 에러가 발생했습니다. error : {e}")

# except 문법 또한 if / elif와 같이 연달아서 작성할 수 있습니다.