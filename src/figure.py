"""Модуль, который содержит реализацию класса Figure."""

from src.coord import Coord
from src.enums import Color, FigureType


class Figure:
    """Реализация шахматной фигуры."""

    def __init__(self, type_of_figure: FigureType, color: Color, coord: Coord) -> None:
        """Инициализирует поля объекта.

        Args:
            type_of_figure(FigureType): Строковая константа из перечисления FigureType;
            color(Color): Строковая константа из перечисления Color;
            coord(Coord): Координаты фигуры.
        """
        self.color: Color = color
        self.type: FigureType = type_of_figure
        self.coord: Coord = coord
        self.moves: list = []

    def generate_moves(self, cord_of_king: Coord, board: list[list[str]]) -> None:
        if self.type == FigureType.rook:
            pass

    def check_to_king(self, color_of_king: Color, coord_of_king: Coord, board: list[list[str]]) -> bool:
        if color_of_king == Color.white:
            my_case = True
        else:
            my_case = False

        # rook/queen
        for x in range(coord_of_king.x + 1, 8):
            cell = board[coord_of_king.y][x]
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
            cell = board[coord_of_king.y][minus_x]
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
            cell = board[y][coord_of_king.x]
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
            cell = board[minus_y][coord_of_king.x]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'R':
                        return True
                    break

        # bishop/queen
        for shift in range(1, min(7 - coord_of_king.x, 7 - coord_of_king.y) + 1):
            cell = board[coord_of_king.y + shift][coord_of_king.x + shift]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'B':
                        return True
                    break

        for shift in range(1, min(7 - coord_of_king.x, coord_of_king.y) + 1):
            cell = board[coord_of_king.y - shift][coord_of_king.x + shift]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'B':
                        return True
                    break

        for shift in range(1, min(coord_of_king.x, 7 - coord_of_king.y) + 1):
            cell = board[coord_of_king.y + shift][coord_of_king.x - shift]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'B':
                        return True
                    break

        for shift in range(1, min(coord_of_king.x, coord_of_king.y) + 1):
            cell = board[coord_of_king.y - shift][coord_of_king.x - shift]
            if cell != '':
                if cell.isupper() == my_case:
                    break
                else:
                    if cell.upper() == 'Q':
                        return True
                    if cell.upper() == 'B':
                        return True
                    break

        # knight
        for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)):
            if 0 < coord_of_king.y + dy < 8 and 0 < coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell.upper() == 'N':
                            return True

        # black pawn
        for dx, dy in ((1, -1), (-1, -1)):
            if 0 < coord_of_king.y + dy < 8 and 0 < coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'p':
                            return True
        # white pawn
        for dx, dy in ((1, 1), (-1, 1)):
            if 0 < coord_of_king.y + dy < 8 and 0 < coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'P':
                            return True

        # king
        for dx, dy in ((1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 < coord_of_king.y + dy < 8 and 0 < coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.upper() == 'K':
                        return True

        return False
