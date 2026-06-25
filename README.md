# Chess Engine

Веб-приложение для игры в шахматы против простого AI-соперника. Пользователь выбирает цвет, делает ход на интерактивной доске, после чего компьютер выбирает случайный ход из сгенерированных легальных ходов.

Web application for playing chess against a simple AI opponent. The user chooses a color, makes a move on the interactive board, and the computer replies with a random move from generated legal moves.

---

### Возможности

- Регистрация и вход пользователя.
- Выбор цвета перед началом партии.
- Интерактивная шахматная доска в браузере.
- Генерация доступных ходов для текущей стороны.
- Случайный ход компьютера после хода игрока.
- Отображение результата партии при мате или пате.
- SQLite-база для хранения пользователей.

### Требования

- Python 3.10 или новее.
- `pip`.
- Виртуальное окружение рекомендуется.

### Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Для Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### База данных и миграции

Проект использует SQLite. Файл базы данных создается автоматически при запуске приложения:

```text
chess_db.db
```

Отдельной системы миграций сейчас нет. Таблица `users` создается функцией `init_db()` из `src/server/db.py` при импорте `src/server/main_app.py`.

Чтобы пересоздать локальную базу с нуля, остановите приложение и удалите файл:

```bash
rm chess_db.db
```

После следующего запуска приложения база и таблица пользователей будут созданы заново.

### Запуск приложения

```bash
python -m src.server.main_app
```

По умолчанию приложение слушает:

```text
http://0.0.0.0:5000
```

Обычно в браузере удобно открыть:

```text
http://127.0.0.1:5000
```

### Запуск тестов

```bash
python -m pytest -q
```

### Проверка синтаксиса

```bash
python -m compileall src tests
```

### Структура проекта

```text
src/
  chess.py              Основная логика шахматной доски и применения ходов
  position.py           Генерация и проверка ходов позиции
  figure.py             Логика ходов фигур
  coord.py              Координаты доски
  enums.py              Перечисления цветов и типов фигур
  server/
    main_app.py         Flask-приложение и игровые маршруты
    db.py               SQLite-инициализация и запросы пользователей
    utils.py            Проверка паролей
    templates/          HTML-шаблоны
tests/
  test_chess.py         Тесты парсинга шахматной доски
  test_position.py      Тесты проверок позиции и шаха
requirements.txt        Python-зависимости
```

### Основные маршруты

- `/` - страница входа.
- `/registration` - регистрация.
- `/main_page` - главное меню после входа.
- `/game?color=white` - новая партия за белых.
- `/game?color=black` - новая партия за черных; компьютер делает первый ход.
- `/game/move` - JSON API для выполнения хода игрока и ответа компьютера.
- `/logout` - выход.

### Типичный сценарий разработки

```bash
source .venv/bin/activate
python -m compileall src tests
python -m pytest -q
python -m src.server.main_app
```

### Частые проблемы

Если команда `pytest` не найдена, используйте:

```bash
python -m pytest -q
```

Если модуль `flask` не найден, установите зависимости:

```bash
python -m pip install -r requirements.txt
```

Если порт `5000` занят, измените порт в конце файла `src/server/main_app.py`:

```python
app.run(host='0.0.0.0', port=5000)
```

---

### Features

- User registration and login.
- Color selection before starting a game.
- Interactive chessboard in the browser.
- Legal move generation for the active side.
- Random computer move after the player's move.
- Game result display for checkmate or stalemate.
- SQLite database for users.

### Requirements

- Python 3.10 or newer.
- `pip`.
- A virtual environment is recommended.

### Installation

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

For Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Database and migrations

The project uses SQLite. The database file is created automatically when the application starts:

```text
chess_db.db
```

There is no separate migration framework at the moment. The `users` table is created by `init_db()` from `src/server/db.py` when `src/server/main_app.py` is imported.

To recreate the local database from scratch, stop the application and remove the file:

```bash
rm chess_db.db
```

The database and users table will be created again on the next application start.

### Running the application

```bash
python -m src.server.main_app
```

By default, the application listens on:

```text
http://0.0.0.0:5000
```

In a local browser, open:

```text
http://127.0.0.1:5000
```

### Running Tests

```bash
python -m pytest -q
```

### Syntax Check

```bash
python -m compileall src tests
```

### Project structure

```text
src/
  chess.py              Core board logic and move application
  position.py           Position move generation and checks
  figure.py             Piece move logic
  coord.py              Board coordinates
  enums.py              Color and piece type enums
  server/
    main_app.py         Flask application and game routes
    db.py               SQLite initialization and user queries
    utils.py            Password validation
    templates/          HTML templates
tests/
  test_chess.py         Board parsing tests
  test_position.py      Position and check detection tests
requirements.txt        Python dependencies
```

### Main routes

- `/` - login page.
- `/registration` - registration.
- `/main_page` - main menu after login.
- `/game?color=white` - new game as White.
- `/game?color=black` - new game as Black; the computer makes the first move.
- `/game/move` - JSON API for applying the player's move and the computer reply.
- `/logout` - log out.

### Typical development workflow

```bash
source .venv/bin/activate
python -m compileall src tests
python -m pytest -q
python -m src.server.main_app
```

### Troubleshooting

If `pytest` is not found, use:

```bash
python -m pytest -q
```

If the `flask` module is not found, install dependencies:

```bash
python -m pip install -r requirements.txt
```

If port `5000` is already in use, change the port at the bottom of `src/server/main_app.py`:

```python
app.run(host='0.0.0.0', port=5000)
```
