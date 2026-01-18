from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def input_page():
    return render_template('input_page.html'), 200


@app.route('/game')
def game():
    return 'game', 200


@app.route('/registration', methods=['POST'])
def registration():
    print(1)
    return 'registration', 201


@app.route('/registration', methods=['GET'])
def registration_page():
    print(1)
    return render_template('registration.html')


@app.route('/print_name_and_password', methods=['POST'])
def print_name_and_password():
    data = request.json
    print(data.get('login'))
    print(data['password'])
    print(data)
    return ''


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
