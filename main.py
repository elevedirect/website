import requests
from flask import Flask, render_template, send_file, request, redirect

app = Flask('EleveDirect Website')


@app.route('/')
def index():
    news_title, news_content = requests.get('https://raw.githubusercontent.com/elevedirect/app/master/CHANGELOG.md').content.decode().split('---')
    return render_template('index.html', title=news_title, content=news_content)


@app.route('/static/phone.gif')
def reload_gif():
    return send_file('static/phone.gif'), 200


if __name__ == '__main__':
    app.run(debug=True, port=5050, host='0.0.0.0') # ssl_context=('certs/elevedirect_cert.pem', 'certs/elevedirect_key.pem')
