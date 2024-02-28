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
        
members = []

# member1, member2 자체가 인스턴스 = 객체
member1 = Member('이창섭', 'changsub', 1234)
member2 = Member('이지은', 'jieun', 1234)
member3 = Member('김민정', 'minjeong', 1234)

members.append(member1)
members.append(member2)
members.append(member3)

for member in members:
    member.display()
    # print(member.name)


'''
6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
    1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
    2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모두 프린트 해주세요
'''
posts = []

author1 = Post('버거킹', '햄버거의 왕께서 만드신 버거', member1)
author2 = Post('허니버터칩', '한때 품절 대란', member1)
author3 = Post('신라면', '제일 무난하게 맛있어요', member1)
author4 = Post('오트밀', '인간사료', member2)
author5 = Post('불닭볶음면', '먹을때는 행복하지만..', member2)
author6 = Post('맥도날드', '맥도날드씨가 만드신 희대의 역!작! 이 햄버거', member2)
auhtor7 = Post('무파마', '마늘 더 넣으면 맛있어요', member3)
author8 = Post('맘스터치', "어머니께서 직접 만드신 고향의 맛 '그' 햄버거", member3)
author9 = Post('포카칩', '감 자 칩', member3)

posts.append(author1)
posts.append(author2)
posts.append(author3)
posts.append(author4)
posts.append(author5)
posts.append(author6)
posts.append(auhtor7)
posts.append(author8)
posts.append(author9)

for post in posts:
    print(f'')