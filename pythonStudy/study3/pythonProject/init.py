# class에 __init__메소드를 사용할 경우 인스턴스 생성 시 해당 메소드가 실행된다.
class CookieFrame():
    def __init__(self, name):
        print(f"생성 된 과자의 이름은 {name} 입니다!")
        self.name = name

cookie1 = CookieFrame("cookie1") # 생성 된 과자의 이름은 cookie1 입니다!
cookie2 = CookieFrame("cookie2") # 생성 된 과자의 이름은 cookie2 입니다!