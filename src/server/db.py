import sqlite3

DB_NAME = "chess_db.db"


def init_db() -> None:
    connect = sqlite3.connect(DB_NAME)

    cursor = connect.cursor()

    cursor.execute(
        '''
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login  TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        '''
    )
    connect.commit()

    connect.close()


def insert_data(login: str, password: str) -> None:
    connect = sqlite3.connect(DB_NAME)

    cursor = connect.cursor()

    cursor.execute(
        f'''
            INSERT INTO users (login, password)
            VALUES ('{login}', '{password}')
        
        '''
    )

    connect.commit()

    connect.close()


def is_exist(login: str) -> bool:
    connect = sqlite3.connect(DB_NAME)

    connect.row_factory = sqlite3.Row

    cursor = connect.cursor()

    result = cursor.execute(
        f'''
            SELECT *
            FROM users
            WHERE login = "{login}"
        '''
    )

    rows = result.fetchall()
    connect.close()

    return bool(rows)


def select_password(login: str) -> str:
    connect = sqlite3.connect(DB_NAME)

    connect.row_factory = sqlite3.Row

    cursor = connect.cursor()

    result = cursor.execute(
        f'''
            SELECT password
            FROM users
            WHERE login = "{login}"
        '''
    )

    rows = result.fetchall()
    connect.close()
    return rows[0]['password']


