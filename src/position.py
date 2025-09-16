"""Модуль, содержащий реализацию класса Position."""

from src.coord import Coord
from src.enums import Color
from src.figure import Figure


class Position:
    """Класс, реализующий шахматную позицию."""

    def __init__(self) -> None:
        """Инициализирует поля объекта значениями по умолчанию."""
        self.coord_of_white_king: Coord | None = None
        self.coord_of_black_king: Coord | None = None
        self.white_figures: list[Figure] = []
        self.black_figures: list[Figure] = []
        self.board: list[list[str]] = []
        self.coord_of_en_passant: Coord | None = None
        self.order_of_move: str = 'w'
        self.is_mate: bool = True

    def check_to_king(self, color_of_king: Color) -> bool:
        if color_of_king == Color.white:
            my_case = True
            coord_of_king = self.coord_of_white_king

        else:
            my_case = False
            coord_of_king = self.coord_of_black_king

        # rook/queen
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

        # bishop/queen
        for shift in range(1, min(7 - coord_of_king.x, 7 - coord_of_king.y) + 1):
            cell = self.board[coord_of_king.y + shift][coord_of_king.x + shift]
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
            cell = self.board[coord_of_king.y - shift][coord_of_king.x + shift]
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
            cell = self.board[coord_of_king.y + shift][coord_of_king.x - shift]
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
            cell = self.board[coord_of_king.y - shift][coord_of_king.x - shift]
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
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = self.board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell.upper() == 'N':
                            return True

        # black pawn
        for dx, dy in ((1, -1), (-1, -1)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = self.board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'p':
                            return True
        # white pawn
        for dx, dy in ((1, 1), (-1, 1)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = self.board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'P':
                            return True

        # king
        for dx, dy in ((1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = self.board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.upper() == 'K':
                        return True

        return False

    def past_pawn(self) -> bool:
        pass

    def generate_general_moves(self) -> None:
        """Перебор всех белых и черных фигур, вызов метод generate_moves() для каждой фигуры."""
        if self.order_of_move == 'w':
            for white_figure in self.white_figures:
                white_figure.generate_moves(self.coord_of_white_king, self.coord_of_en_passant, self.board, True, True)
                if white_figure.moves:
                    self.is_mate = False

        else:
            for black_figure in self.black_figures:
                black_figure.generate_moves(self.coord_of_black_king, self.coord_of_en_passant, self.board, True, True)
                if black_figure.moves:
                    self.is_mate = False
