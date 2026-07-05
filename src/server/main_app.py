import random

from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from src.engine.chess import Chess
from src.engine.enums import Color
from src.server.db import init_db, insert_data, is_exist, select_password
from src.server.utils import checking_password_security

app = Flask(__name__)

app.secret_key = 'secret_key'

init_db()

INITIAL_GAME_FEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
PLAYER_COLORS = {"white", "black"}


def generated_moves_for(fen: str) -> tuple[Chess, dict[str, list]]:
    chess = Chess(fen)
    chess.position.generate_general_moves()
    return chess, chess.get_moves_for_active_color()


def random_move_from(moves: dict[str, list]) -> tuple[int, int, int, int] | None:
    move_pairs = [
        (from_square, to_square)
        for from_square, destinations in moves.items()
        for to_square in destinations
    ]
    if not move_pairs:
        return None

    from_square, to_square = random.choice(move_pairs)
    from_y, from_x = [int(value) for value in from_square.split(',')]
    to_y, to_x = [int(value) for value in to_square.split(',')]
    return from_y, from_x, to_y, to_x


def move_payload(from_y: int, from_x: int, to_y: int, to_x: int) -> dict:
    return {'from': [from_y, from_x], 'to': [to_y, to_x]}


def active_color_name(chess: Chess) -> str:
    return 'white' if chess.position.order_of_move == 'w' else 'black'


def game_result(chess: Chess, moves: dict[str, list]) -> dict | None:
    if any(moves.values()):
        return None

    color_to_move = active_color_name(chess)
    king_color = Color.white if color_to_move == 'white' else Color.black
    is_check = chess.position.check_to_king(king_color)

    if is_check:
        winner = 'black' if color_to_move == 'white' else 'white'
        return {
            'game_over': True,
            'type': 'checkmate',
            'winner': winner,
            'message': f"Мат. Победили {'белые' if winner == 'white' else 'чёрные'}."
        }

    return {
        'game_over': True,
        'type': 'stalemate',
        'winner': None,
        'message': 'Пат. Ничья.'
    }


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
    player_color = request.args.get('color') or session.get('player_color', 'white')
    if player_color not in PLAYER_COLORS:
        player_color = 'white'

    session['player_color'] = player_color
    current_fen = INITIAL_GAME_FEN
    opening_ai_move = None

    chess, main_color_moves = generated_moves_for(current_fen)
    if player_color == 'black':
        ai_move = random_move_from(main_color_moves)
        if ai_move is not None:
            ai_from_y, ai_from_x, ai_to_y, ai_to_x = ai_move
            current_fen = chess.apply_move(ai_from_y, ai_from_x, ai_to_y, ai_to_x)
            opening_ai_move = move_payload(ai_from_y, ai_from_x, ai_to_y, ai_to_x)
            chess, main_color_moves = generated_moves_for(current_fen)

    session['game_fen'] = current_fen
    result = game_result(chess, main_color_moves)

    return render_template(
        'game.html',
        fen=current_fen,
        all_possible_moves=main_color_moves,
        player_color=player_color,
        ai_move=opening_ai_move,
        game_result=result
    )


@app.route('/game/move', methods=['POST'])
def make_game_move():
    if "user" not in session:
        return jsonify({'error': 'not_authorized'}), 401

    data = request.get_json(silent=True) or {}
    try:
        from_y = int(data['from']['row'])
        from_x = int(data['from']['col'])
        to_y = int(data['to']['row'])
        to_x = int(data['to']['col'])
    except (KeyError, TypeError, ValueError):
        return jsonify({'error': 'incorrect_move_payload'}), 400

    current_fen = session.get('game_fen', INITIAL_GAME_FEN)
    chess, _ = generated_moves_for(current_fen)

    try:
        after_player_fen = chess.apply_move(from_y, from_x, to_y, to_x, data.get('promotion'))
    except ValueError as error:
        return jsonify({'error': str(error)}), 400

    chess, ai_moves = generated_moves_for(after_player_fen)
    result = game_result(chess, ai_moves)
    if result is not None:
        session['game_fen'] = after_player_fen
        return jsonify({
            'fen': after_player_fen,
            'all_possible_moves': {},
            'player_move': move_payload(from_y, from_x, to_y, to_x),
            'ai_move': None,
            'game_result': result,
            'game_over': True
        })

    ai_move = random_move_from(ai_moves)
    if ai_move is None:
        session['game_fen'] = after_player_fen
        return jsonify({
            'fen': after_player_fen,
            'all_possible_moves': {},
            'player_move': move_payload(from_y, from_x, to_y, to_x),
            'ai_move': None,
            'game_result': result,
            'game_over': True
        })

    ai_from_y, ai_from_x, ai_to_y, ai_to_x = ai_move
    after_ai_fen = chess.apply_move(ai_from_y, ai_from_x, ai_to_y, ai_to_x)
    chess, player_moves = generated_moves_for(after_ai_fen)
    result = game_result(chess, player_moves)
    session['game_fen'] = after_ai_fen

    return jsonify({
        'fen': after_ai_fen,
        'all_possible_moves': player_moves,
        'player_move': move_payload(from_y, from_x, to_y, to_x),
        'ai_move': move_payload(ai_from_y, ai_from_x, ai_to_y, ai_to_x),
        'game_result': result,
        'game_over': result is not None
    })


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
