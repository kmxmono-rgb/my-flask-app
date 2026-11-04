from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '嗨！我的第一個 Flask 網站已經成功在 Render 運行了！'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
