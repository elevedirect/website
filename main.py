import requests
from flask import Flask, render_template

app = Flask('EleveDirect Website')


@app.route('/')
def index():
    news_title, news_content = requests.get('https://raw.githubusercontent.com/elevedirect/app/master/CHANGELOG.md').content.decode().split('---')
    return render_template('index.html', title=news_title, content=news_content)


if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0')
