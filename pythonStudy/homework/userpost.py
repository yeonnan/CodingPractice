'''
**추가 도전 과제:**

1. input을 이용하여 Member 인스턴스 만드는것을 사용자가 터미널에서 할 수 있게 해주세요.
2. post도 터미널에서 생성할 수 있게 해주세요.
3. (심화)비밀번호 해싱이 무엇인지 공부한 후 hashlib 라이브러리를 써서 회원 비밀번호를 해시화하여 저장하게 해주세요.

**평가**

- 클래스와 인스턴스 개념을 설명할 수 있는가?
- 메소드와 어트리뷰트(속성)을 설명할 수 있는가?
- 클래스를 정의할 수 있는가?
- 인스턴스를 생성할 수 있는가?
'''

class Member:
    def __init__(self, name, username, password):
        # 인스턴스 변수
        self.name = name
        self.username = username
        self.password = password
    def display(self):
        print(f'회원이름 : {self.name}, id : {self.username}')

        
class Post:
    def __init__(self, title, content,author):
        self.title = title     # 제목
        self.content = content     # 내용
        self.author = author    # 작성자 - 회원의 `username` 이 저장되어야 함
        pass

members = []

member1 = Member('이창섭', 'changsub', 1234)
member2 = Member('이지은', 'jieun', 1234)
member3 = Member('김민정', 'minjeong', 1234)

members.append(member1)
members.append(member2)
members.append(member3)

for member in members:
    print(member.name)


'''
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
'''
posts = []