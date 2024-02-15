# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# db 기본 코드
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(10000), nullable=False)

    def __repr__(self):
        return f'{self.title} {self.artist} 추천 by {self.username}'

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    name = 'aaa'
    motto = "고양이가 세상을 구한다."

    context = {
        "name": name,
        "motto": motto,
    }
    return render_template('motto.html', data=context)

@app.route("/music/")
def music():
    song_list = Song.query.all()
    return render_template('music.html', data = song_list)

@app.route("/music/<username>/")    # username을 <>에 넣어서 사용하면 변수처럼 가져와서 데이터화해서 사용 가능하다.
def render_music_filter(username):
    filter_list = Song.query.filter_by(username = username).all()
    return render_template('music.html', data = filter_list)

@app.route("/iloveyou/<name>/")
def iloveyou(name):
    motto = f"{name}야 난 너뿐이야!"

    context = {
        'name': name,
        'motto': motto,
    }
    return render_template('motto.html', data=context)

@app.route("/music/create/")
def music_create():
    # form에서 보낸 데이터 받아오기
    username_receive = request.args.get("username")     # username : music.html에서 지정해줬던 것
    title_receive = request.args.get("title")    
    artist_receive = request.args.get("artist")    
    image_receive = request.args.get("image_url")     

    # 데이터를 db에 저장하기
    song = Song(username = username_receive, title = title_receive, artist = artist_receive, image_url = image_receive)
    db.session.add(song)    # 추가
    db.session.commit()     # 확정
    return redirect(url_for('render_music_filter', username = username_receive))

if __name__ == "__main__":
    app.run(debug=True, port=5001)