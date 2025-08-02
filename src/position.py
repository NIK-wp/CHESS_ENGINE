"""Модуль, содержащий реализацию класса Position."""

from src.coord import Coord
from src.enums import Color
from src.figure import Figure


class Position:
    """Класс, реализующий шахматную позицию."""

    def __init__(self) -> None:
        """Инициализирует поля объекта значениями по умолчанию."""
        self.cord_of_white_king: Coord | None = None
        self.cord_of_black_king: Coord | None = None
        self.white_figures: list[Figure] = []
        self.black_figures: list[Figure] = []
        self.board: list[list[str]] = []

    def check_to_king(self, color_of_king: Color) -> bool:
        if color_of_king == Color.white:
            my_case = True
            coord_of_king = self.cord_of_white_king

        else:
            my_case = False
            coord_of_king = self.cord_of_black_king

        for x in range(coord_of_king.x + 1, 8):
            cell = self.board[coord_of_king.y][x]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'R':
                        return True
                    break

        for minus_x in range(coord_of_king.x - 1, -1, -1):
            cell = self.board[coord_of_king.y][minus_x]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'R':
                        return True
                    break

        for y in range(coord_of_king.y + 1, 8):
            cell = self.board[y][coord_of_king.x]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'R':
                        return True
                    break

        for minus_y in range(coord_of_king.y - 1, -1, -1):
            cell = self.board[minus_y][coord_of_king.x]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'R':
                        return True
                    break

        return False

    def past_pawn(self) -> bool:
        pass
