import os

from flask import Flask, render_template, redirect
app = Flask(__name__)


# я обещал никогда не браться за питон но.......
# ATTENTION я противник питона, но пишу на нем, поэтому дальше ожидай лютое легаси
@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/')
def redir():
    return redirect('http://127.0.0.1:5000/login', code=302)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
