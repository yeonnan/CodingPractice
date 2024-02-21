# result = [] 를 이용하여 'kia', 'hyundai'를 대문자로 바꾸기

cars = ['audi', 'bmw', 'subaru', 'kia', 'toyota', 'hyundai']

result = []

for car in cars:
    if (car == 'kia' or car == 'hyundai'):
        result.append(car.upper())

print(result)

# if (car == 'kia' or car == 'hyundai'): 에서 or이 아니라 and면 어떻게 될까?
# and는 두 조건이 모두 만족해야 참이 되는데, 기아와 현대는 동시에 참이 될 수 없기 때문에 result에는 아무 값도 추가되지 않는다.