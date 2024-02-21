from datetime import datetime, timedelta

# 현재 날짜 및 시간 출력
print(datetime.now()) # 2023-02-22 15:55:32.277095

# datetime의 format code 더 제세한건 여기서 확인 가능합니다.
'''
%y : 두 자리 연도 / 20, 21, 22
%Y : 네 자리 연도 / 2020, 2021, 2022
%m : 두 자리 월 / 01, 02 ... 11 ,12
%d : 두 자리 일 / 01, 02 ...  30, 31
%I : 12시간제 시간 / 01, 02 ... 12
%H : 24시간제의 시간 / 00, 01 ... 23
%M : 두 자리 분 / 00, 01 ... 58, 59
%S : 두 자리 초 / 00, 01 ... 58, 59
'''

# string을 datetime 날짜로 변경하기
string_datetime = "23/12/25 13:20"
datetime_ = datetime.strptime(string_datetime, "%y/%m/%d %H:%M")
print(datetime_) # 2023-12-25 13:20:00

# datetime 날짜를 string으로 변환하기
now = datetime.now()
string_datetime = datetime.strftime(now, "%y/%m/%d %H:%M:%S")
print(string_datetime) # 22/09/04 04:04

# 3일 전 날짜 구하기
three_days_ago = datetime.now() - timedelta(days=3)
print(three_days_ago) # 2023-02-19 16:27:52.526502