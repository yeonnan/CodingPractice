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
        
post_contents = [
    {'title' : '버거킹', 'content' : '햄버거의 왕께서 만드신 버거', 'author' : member1},
    {'title' : '허니버터칩', 'content' : '한때 품절 대란 과자', 'author' : member1},
    {'title' : '신라면', 'content' : '제일 무난하게 맛있어요 라면', 'author' : member1},
    {'title' : '오트밀', 'content' : '인간사료 과자', 'author' : member2},
    {'title' : '불닭볶음면', 'content' : '먹을때는 행복하지만.. 라면', 'author' : member2},
    {'title' : '맥도날드', 'content' : '맥도날드씨가 만드신 희대의 역!작! 이 햄버거', 'author' : member2},
    {'title' : '무파마', 'content' : '마늘 더 넣으면 맛있어요 라면', 'author' : member3},
    {'title' : '맘스터치', 'content' : "어머니께서 직접 만드신 고향의 맛 '그' 햄버거", 'author' : member3},
    {'title' : '포카칩', 'content' : '감 자 칩 과자', 'author' : member3}
]

posts = []

for post_content in post_contents:
    posts.append(
        Post(
            post_content['title'],
            post_content['content'],
            post_content['author'].name
        )
    )
    
# 특정 '유저'가 작성한 게시글의 '제목' 프린트
for post in posts:
    if post.author == '이창섭':
        print(post.title)
        
# ‘특정 단어’가 content에 포함된 게시글의 '제목'을 모두 프린트
# ex) 햄버거, 라면, 과자
word_search = input('검색하고자 하는 단어를 적어주세요 : ')
for post in posts:
    if word_search in post.content:
        print(post.title)