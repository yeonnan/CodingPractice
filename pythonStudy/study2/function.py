def sum(a,b):
    print('더하기')
    return a+b

result = sum(1,2)
print(result)

def bus_rate(age):
    if age > 65:
        print('무료')
    elif age > 20:
        print('성인')
    else:
        print('청소년')

bus_rate(30)

def bus_fee(age):
	if age > 65:
		return 0
	elif age > 20:
		return 1200
	else:
	    return 750

money = bus_fee(15)
print(money)

# 주민 번호를 받아서 성별 출력
def check_gender(pin):
    num = pin.split('-')[1][:1]
    if int(num) % 2 == 0:
        print('여성')
    else:
        print('남성')

check_gender('123456-1234567')  # 남성
check_gender('234567-2345678')  # 여성
check_gender('456789-1234567')  # 남성