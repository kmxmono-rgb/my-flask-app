import os
from flask import Flask, render_template

app = Flask(__name__)


# 1. 首頁
@app.route('/')
def home():
  return render_template('index.html')


# 2. 關於我們頁面
@app.route('/about')
def about():
  return render_template('about.html')


# 3. 聯絡我們頁面
@app.route('/contact')
def contact():
  return render_template('contact.html')


# 整合後的啟動設定：同時支援本地開發與 Render 部署
if __name__ == '__main__':
  # 從環境變數讀取 Port（Render 專用），若讀不到則預設為本地端的 5000
  port = int(os.environ.get('PORT', 5000))

  # host='0.0.0.0' 讓外部網路（Render）可以連線
  # debug=False 在部署時建議關閉，或改用環境變數控制
  app.run(host='0.0.0.0', port=port, debug=False)
