import time

start_time = time.time() # 현재 시간 저장

time.sleep(1) # 1초간 대기

end_time = time.time()

# 코드가 종료된 시간 - 코드가 시작된 시간으로 실행 시간 구하기 (단위 : 초)
print(f"코드 실행 시간 : {end_time-start_time:.5f}") # 코드 실행 시간 : 1.00100