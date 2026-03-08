from flask import Flask, render_template, request, session, redirect, url_for

from src.server.db import init_db, insert_data, is_exist, select_password

app = Flask(__name__)


app.secret_key = 'secret_key'

init_db()


@app.route('/', methods=['GET'])
def input_page():
    return render_template('input_page.html'), 200


@app.route('/input', methods=['POST'])
def input():
    data = request.json
    if not is_exist(data['login']):
        return 'not_authorized', 401
    if data['password'] != select_password(data['login']):
        return 'different_passwords', 400

    session["user"] = data["login"]
    return 'input', 201


@app.route('/print_name_and_password', methods=['POST'])
def print_name_and_password():
    data = request.json
    print(data.get('login'))
    print(data['password'])
    print(data)
    return ''


@app.route('/game')
def game():
    if "user" not in session:
        return redirect(url_for('input_page'))  # ссылаться на функцию а не на роут
    return render_template('game.html'), 200


@app.route('/registration', methods=['GET'])
def registration_page():
    return render_template('registration.html')


@app.route('/registration', methods=['POST'])
def registration():
    data = request.json
    if is_exist(data['login']):
        return 'login_already_exist', 409
    if data['password'] != data['password2']:
        return 'different_passwords', 400

    insert_data(data['login'], data['password'])

    session["user"] = data["login"]
    return 'registrated', 201


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('input_page'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)


