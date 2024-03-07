# 오늘은 2024년 1월 14일 입니다.
year = 2024
month = 1
day = 14

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")

date_string = "오늘은 {}년 {}월 {}일 입니다."
print(date_string.format(year, month, day + 1))

print("저는 {1}, {0}, {2}를 좋아합니다.".format("사과", "포도", "귤"))

###
num1 = 1
num2 = 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num1, num2, num1/num2))