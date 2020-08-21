from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

#local host 5000에 html 파일 연결해보기
@app.route('/')
def home():
    return render_template("page2_calendar2.html")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True) # local host 5000에 들어간다는 의미

