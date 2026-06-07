from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from src.server.db import init_db, insert_data, is_exist, select_password
from src.server.utils import checking_password_security

app = Flask(__name__)

app.secret_key = 'secret_key'

init_db()


@app.route('/', methods=['GET'])
def input_page():
    return render_template('input_page_AI.html'), 200


@app.route('/input', methods=['POST'])
def input():
    data = request.json
    if not is_exist(data['login']):
        return 'not_authorized', 401
    if not check_password_hash(select_password(data['login']), data['password']):
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
        return redirect(url_for('input_page'))
    return render_template('game_AI_full.html'), 200


@app.route('/registration', methods=['GET'])
def registration_page():
    return render_template('registration_AI.html')


@app.route('/registration', methods=['POST'])
def registration():
    data = request.json
    if is_exist(data['login']):
        return 'login_already_exist', 409
    if not checking_password_security(data['password']):
        return 'incorrect_password', 400
    if data['password'] != data['password2']:
        return 'different_passwords', 400

    password_hash = generate_password_hash(data['password'])
    insert_data(data['login'], password_hash)

    session["user"] = data["login"]
    return 'registrated', 201


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('input_page'))


if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5000)
    app.run(host='0.0.0.0', port=5000)
