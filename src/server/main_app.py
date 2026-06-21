from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from src.chess import Chess
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


@app.route('/main_page')
def main_page():
    if "user" not in session:
        return redirect(url_for('input_page'))
    return render_template('main_page.html'), 200


@app.route('/game')
def game():
    if "user" not in session:
        return redirect(url_for('input_page'))
    initial_fen = "8/k7/8/8/8/4R3/8/5K2 w - - 0 1"
    check_board = Chess(initial_fen)
    check_board.position.generate_general_moves()
    # Словарь с ходами: ключ - координата фигуры, значение - список возможных ходов
    # (ключи - строки "row,col", значения - списки строк "row,col")
    main_color_moves = check_board.get_moves_for_active_color()
    # main_color_moves = {
    #     # Белая ладья на (5, 4) - строка 5 (3-я горизонталь), столбец 4 (e)
    #     "5,4": [
    #         # Ходы по вертикали (вверх)
    #         "4,4", "3,4", "2,4", "1,4", "0,4",
    #         # Ходы по вертикали (вниз)
    #         "6,4", "7,4",
    #         # Ходы по горизонтали (влево)
    #         "5,3", "5,2", "5,1", "5,0",
    #         # Ходы по горизонтали (вправо)
    #         "5,5", "5,6", "5,7"
    #     ],
    #
    #     # Белый король на (7, 5) - строка 7 (1-я горизонталь), столбец 5 (f)
    #     "7,5": [
    #         # Ходы вверх
    #         "6,4", "6,5", "6,6",
    #         # Ходы влево-вправо
    #         "7,4", "7,6"
    #     ]
    # }
    return render_template('game.html', fen=initial_fen, all_possible_moves=main_color_moves)


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
