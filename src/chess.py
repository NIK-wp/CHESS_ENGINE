from src.coord import Coord
"""импорт класса Coord из другого файла"""


class Chess:
    """
    Базовый класс для визуализации и логики шахмат

    """
    def __init__(self) -> None:
        """
        Args:
            board: двумерный список для представления шахматной доски

            order_of_move: Отслеживает,чей ход ('white' или 'black')

            castling: Словарь для отслеживания наличия рокировок

            full_move_number: Подсчитывает общее количество ходов в игре

            halfmove_clock: Подсчитывает количество ходов без движения пешек в соответствии с правилом о 50 ходах

            coord_of_en_passant: отслеживает координату хода пешки на 2 клетки вперёд
        """
        self.board: list[list[str]] = [[' ' for _ in range(8)] for _ in range(8)]
        self.order_of_move: str = 'w'
        self.castling: dict = {}
        self.full_move_number: int = 0
        self.halfmove_clock: int = 0
        self.coord_of_en_passant: Coord | None = None

    def show_board(self) -> None:
        """Визуализация шахматной доски."""
        pass

    def parse_fen(self) -> None:
        """Анализ строк FEN Forsyth–Edwards Notation"""
        pass
