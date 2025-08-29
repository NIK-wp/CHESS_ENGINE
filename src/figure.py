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
        self.moves: list[Coord] = []

    def generate_moves(self, coord_of_king: Coord, board: list[list[str]]) -> None:
        """Генерация ходов фигуры

        Args:
            coord_of_king(Coord): Координата короля данного цвета фигуры;
            board(list[list[str]]): шахматная доска;
        """
        if self.color == Color.white:
            my_case = True
        else:
            my_case = False

        # rook and queen
        if self.type == FigureType.rook or self.type == FigureType.queen:

            """Перебор для ладьи вправо"""

            for x in range(self.coord.x + 1, 8):
                cell = board[self.coord.y][x]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y][x]
                        if self.type == FigureType.queen:
                            board[self.coord.y][x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][x] = 'R' if self.color == Color.white else 'r'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y, x))
                        board[self.coord.y][x] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][x] = 'R' if self.color == Color.white else 'r'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y, x))
                    board[self.coord.y][x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'

            """Перебор для ладьи влево"""

            for minus_x in range(self.coord.x - 1, -1, -1):
                cell = board[self.coord.y][minus_x]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y][minus_x]
                        if self.type == FigureType.queen:
                            board[self.coord.y][minus_x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][minus_x] = 'R' if self.color == Color.white else 'r'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y, minus_x))
                        board[self.coord.y][minus_x] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][minus_x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][minus_x] = 'R' if self.color == Color.white else 'r'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y, minus_x))
                    board[self.coord.y][minus_x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'

            """Перебор для ладьи вниз"""

            for y in range(self.coord.y + 1, 8):
                cell = board[y][self.coord.x]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[y][self.coord.x]
                        if self.type == FigureType.queen:
                            board[y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(y, self.coord.x))
                        board[y][self.coord.x] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(y, self.coord.x))
                    board[y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'

            """Перебор для ладьи вверх"""

            for minus_y in range(self.coord.y - 1, -1, -1):
                cell = board[minus_y][self.coord.x]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[minus_y][self.coord.x]
                        if self.type == FigureType.queen:
                            board[minus_y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[minus_y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(minus_y, self.coord.x))
                        board[minus_y][self.coord.x] = fig

                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[minus_y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[minus_y][self.coord.x] = 'R' if self.color == Color.white else 'r'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(minus_y, self.coord.x))
                    board[minus_y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'R' if self.color == Color.white else 'r'

        # bishop and queen
        if self.type == FigureType.bishop or self.type == FigureType.queen:

            """Перебор для слона вправо вниз"""

            for shift in range(1, min(7 - self.coord.x, 7 - self.coord.y) + 1):
                cell = board[self.coord.y + shift][self.coord.x + shift]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y + shift][self.coord.x + shift]
                        if self.type == FigureType.queen:
                            board[self.coord.y + shift][
                                self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y + shift][
                                self.coord.x + shift] = 'B' if self.color == Color.white else 'b'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y + shift, self.coord.x + shift))
                        board[self.coord.y + shift][self.coord.x + shift] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'B'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y + shift][self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y + shift][self.coord.x + shift] = 'B' if self.color == Color.white else 'b'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y + shift, self.coord.x + shift))
                    board[self.coord.y + shift][self.coord.x + shift] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'

            """Перебор для слона вправо вверх"""

            for shift in range(1, min(7 - self.coord.x, self.coord.y) + 1):
                cell = board[self.coord.y - shift][self.coord.x + shift]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y - shift][self.coord.x + shift]
                        if self.type == FigureType.queen:
                            board[self.coord.y - shift][
                                self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y - shift][
                                self.coord.x + shift] = 'B' if self.color == Color.white else 'b'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y - shift, self.coord.x + shift))
                        board[self.coord.y + shift][self.coord.x + shift] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y - shift][
                            self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y - shift][
                            self.coord.x + shift] = 'B' if self.color == Color.white else 'b'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y - shift, self.coord.x + shift))
                    board[self.coord.y - shift][self.coord.x + shift] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'B'

            """Перебор для слона влево вниз"""

            for shift in range(1, min(self.coord.x, 7 - self.coord.y) + 1):
                cell = board[self.coord.y + shift][self.coord.x - shift]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y + shift][self.coord.x - shift]
                        if self.type == FigureType.queen:
                            board[self.coord.y + shift][
                                self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y + shift][
                                self.coord.x - shift] = 'B' if self.color == Color.white else 'b'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y + shift, self.coord.x - shift))
                        board[self.coord.y + shift][self.coord.x - shift] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'
                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y + shift][self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y + shift][self.coord.x - shift] = 'B' if self.color == Color.white else 'b'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y + shift, self.coord.x - shift))
                    board[self.coord.y + shift][self.coord.x - shift] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'

            """ Перебор для слона влево вверх"""

            for shift in range(1, min(self.coord.x, self.coord.y) + 1):
                cell = board[self.coord.y - shift][self.coord.x - shift]
                if cell != '':
                    if cell.isupper() == my_case:
                        break
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        fig = board[self.coord.y - shift][self.coord.x - shift]
                        if self.type == FigureType.queen:
                            board[self.coord.y - shift][
                                self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y - shift][
                                self.coord.x - shift] = 'B' if self.color == Color.white else 'b'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y - shift, self.coord.x - shift))
                        board[self.coord.y - shift][self.coord.x - shift] = fig
                        if self.type == FigureType.queen:
                            board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                        else:
                            board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'

                        break
                else:
                    board[self.coord.y][self.coord.x] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y - shift][self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y - shift][self.coord.x - shift] = 'B' if self.color == Color.white else 'b'

                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y - shift, self.coord.x - shift))
                    board[self.coord.y - shift][self.coord.x - shift] = ''
                    if self.type == FigureType.queen:
                        board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
                    else:
                        board[self.coord.y][self.coord.x] = 'B' if self.color == Color.white else 'b'


        # knight
        elif self.type == FigureType.knight:
            for dx, dy in ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)):
                if 0 <= self.coord.y + dy < 8 and 0 <= self.coord.x + dx < 8:
                    cell = board[self.coord.y + dy][self.coord.x + dx]
                    if cell != '':
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = ''
                            fig = board[self.coord.y + dy][self.coord.x + dx]
                            board[self.coord.y + dy][
                                self.coord.x + dx] = 'N' if self.color == Color.white else 'n'
                            if not self.check_to_king(self.color, coord_of_king, board):
                                self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                            board[self.coord.y + dy][self.coord.x + dx] = fig
                            board[self.coord.y][self.coord.x] = 'N' if self.color == Color.white else 'n'
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        board[self.coord.y + dy][
                            self.coord.x + dx] = 'N' if self.color == Color.white else 'n'
                        if not self.check_to_king(self.color, coord_of_king, board):
                            self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                        board[self.coord.y + dy][self.coord.x + dx] = ''
                        board[self.coord.y][self.coord.x] = 'N' if self.color == Color.white else 'n'

        # king
        elif self.type == FigureType.king:
            for dx, dy in ((1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= self.coord.y + dy < 8 and 0 <= self.coord.x + dx < 8:
                    cell = board[self.coord.y + dy][self.coord.x + dx]
                    if cell != '':
                        if cell.isupper() != my_case:
                            board[self.coord.y][self.coord.x] = ''
                            fig = board[self.coord.y + dy][self.coord.x + dx]
                            board[self.coord.y + dy][
                                self.coord.x + dx] = 'K' if self.color == Color.white else 'k'
                            if not self.check_to_king(self.color, Coord(self.coord.y + dy, self.coord.x + dx), board):
                                self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                            board[self.coord.y + dy][self.coord.x + dx] = fig
                            board[self.coord.y][self.coord.x] = 'K' if self.color == Color.white else 'k'
                    else:
                        board[self.coord.y][self.coord.x] = ''
                        board[self.coord.y + dy][
                            self.coord.x + dx] = 'K' if self.color == Color.white else 'k'
                        if not self.check_to_king(self.color, Coord(self.coord.y + dy, self.coord.x + dx), board):
                            self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                        board[self.coord.y + dy][self.coord.x + dx] = ''
                        board[self.coord.y][self.coord.x] = 'K' if self.color == Color.white else 'k'

        # # queen
        # elif self.type == FigureType.queen:
        #     for shift in range(1, min(7 - self.coord.x, 7 - self.coord.y) + 1):
        #         cell = board[self.coord.y + shift][self.coord.x + shift]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y + shift][self.coord.x + shift]
        #                 board[self.coord.y + shift][
        #                     self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y + shift, self.coord.x + shift))
        #                 board[self.coord.y + shift][self.coord.x + shift] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[self.coord.y + shift][self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y + shift, self.coord.x + shift))
        #             board[self.coord.y + shift][self.coord.x + shift] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #
        #     for shift in range(1, min(7 - self.coord.x, self.coord.y) + 1):
        #         cell = board[self.coord.y - shift][self.coord.x + shift]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y - shift][self.coord.x + shift]
        #                 board[self.coord.y - shift][
        #                     self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y - shift, self.coord.x + shift))
        #                 board[self.coord.y - shift][self.coord.x + shift] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[self.coord.y - shift][
        #                 self.coord.x + shift] = 'Q' if self.color == Color.white else 'q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y - shift, self.coord.x + shift))
        #             board[self.coord.y - shift][self.coord.x + shift] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #
        #     for shift in range(1, min(self.coord.x, 7 - self.coord.y) + 1):
        #         cell = board[self.coord.y + shift][self.coord.x - shift]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y + shift][self.coord.x - shift]
        #                 board[self.coord.y + shift][
        #                     self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y + shift, self.coord.x - shift))
        #                 board[self.coord.y + shift][self.coord.x - shift] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[self.coord.y + shift][self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y + shift, self.coord.x - shift))
        #             board[self.coord.y + shift][self.coord.x - shift] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #
        #     for shift in range(1, min(self.coord.x, self.coord.y) + 1):
        #         cell = board[self.coord.y - shift][self.coord.x - shift]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y - shift][self.coord.x - shift]
        #                 board[self.coord.y - shift][
        #                     self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y - shift, self.coord.x - shift))
        #                 board[self.coord.y - shift][self.coord.x - shift] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[self.coord.y - shift][self.coord.x - shift] = 'Q' if self.color == Color.white else 'q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y - shift, self.coord.x - shift))
        #             board[self.coord.y - shift][self.coord.x - shift] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #
        #     for x in range(self.coord.x + 1, 8):
        #         cell = board[self.coord.y][x]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y][x]
        #                 # if self.type == FigureType.queen:
        #                 #     board[self.coord.y][x] = 'Q' if self.color == Color.white else 'q'
        #                 # else:
        #                 board[self.coord.y][x] = 'Q' if self.color == Color.white else 'Q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y, x))
        #                 board[self.coord.y][x] = fig
        #                 # if self.type == FigureType.queen:
        #                 #     board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 # else:
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             # if self.type == FigureType.queen:
        #             #     board[self.coord.y][x] = 'Q' if self.color == Color.white else 'q'
        #             # else:
        #             board[self.coord.y][x] = 'Q' if self.color == Color.white else 'Q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y, x))
        #             board[self.coord.y][x] = ''
        #             # if self.type == FigureType.queen:
        #             #     board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #             # else:
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #     #q
        #     for minus_x in range(self.coord.x - 1, -1, -1):
        #         cell = board[self.coord.y][minus_x]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[self.coord.y][minus_x]
        #                 # if self.type == FigureType.queen:
        #                 #     board[self.coord.y][minus_x] = 'Q' if self.color == Color.white else 'q'
        #                 # else:
        #                 board[self.coord.y][minus_x] = 'Q' if self.color == Color.white else 'Q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(self.coord.y, minus_x))
        #                 board[self.coord.y][minus_x] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[self.coord.y][minus_x] = 'Q' if self.color == Color.white else 'Q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(self.coord.y, minus_x))
        #             board[self.coord.y][minus_x] = ''
        #             # if self.type == FigureType.queen:
        #             #     board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #             # else:
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #
        #     for y in range(self.coord.y + 1, 8):
        #         cell = board[y][self.coord.x]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[y][self.coord.x]
        #                 # if self.type == FigureType.queen:
        #                 #     board[y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 # else:
        #                 board[y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(y, self.coord.x))
        #                 board[y][self.coord.x] = fig
        #                 # if self.type == FigureType.queen:
        #                 #     board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'q'
        #                 # else:
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(y, self.coord.x))
        #             board[y][self.coord.x] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #
        #     for minus_y in range(self.coord.y - 1, -1, -1):
        #         cell = board[minus_y][self.coord.x]
        #         if cell != '':
        #             if cell.isupper() == my_case:
        #                 break
        #             else:
        #                 board[self.coord.y][self.coord.x] = ''
        #                 fig = board[minus_y][self.coord.x]
        #                 board[minus_y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 if not self.check_to_king(self.color, coord_of_king, board):
        #                     self.moves.append(Coord(minus_y, self.coord.x))
        #                 board[minus_y][self.coord.x] = fig
        #                 board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #                 break
        #         else:
        #             board[self.coord.y][self.coord.x] = ''
        #             board[minus_y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'
        #             if not self.check_to_king(self.color, coord_of_king, board):
        #                 self.moves.append(Coord(minus_y, self.coord.x))
        #             board[minus_y][self.coord.x] = ''
        #             board[self.coord.y][self.coord.x] = 'Q' if self.color == Color.white else 'Q'

        # pawn
        elif self.type == FigureType.pawn:
            # white
            if self.color == Color.white:
                for dx, dy in ((1, -1), (-1, -1)):
                    if 0 <= self.coord.y + dy < 8 and 0 <= self.coord.x + dx < 8:
                        cell = board[self.coord.y + dy][self.coord.x + dx]
                        if cell != '':
                            if cell.isupper() != my_case:
                                board[self.coord.y][self.coord.x] = ''
                                fig = board[self.coord.y + dy][self.coord.x + dx]
                                board[self.coord.y + dy][
                                    self.coord.x + dx] = 'P'
                                if not self.check_to_king(self.color, coord_of_king, board):
                                    self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                                board[self.coord.y + dy][self.coord.x + dx] = fig
                                board[self.coord.y][self.coord.x] = 'P'

                cell = board[self.coord.y - 1][self.coord.x]
                if cell == '':
                    board[self.coord.y][self.coord.x] = ''
                    board[self.coord.y - 1][
                        self.coord.x] = 'P'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y - 1, self.coord.x))
                    board[self.coord.y - 1][self.coord.x] = ''
                    board[self.coord.y][self.coord.x] = 'P'

                    if self.coord.y == 6:
                        if board[self.coord.y - 2][self.coord.x] == '':
                            board[self.coord.y][self.coord.x] = ''
                            board[self.coord.y - 2][
                                self.coord.x] = 'P'
                            if not self.check_to_king(self.color, coord_of_king, board):
                                self.moves.append(Coord(self.coord.y - 2, self.coord.x))
                            board[self.coord.y - 2][self.coord.x] = ''
                            board[self.coord.y][self.coord.x] = 'P'

            # black
            else:
                for dx, dy in ((1, 1), (-1, 1)):
                    if 0 <= self.coord.y + dy < 8 and 0 <= self.coord.x + dx < 8:
                        cell = board[self.coord.y + dy][self.coord.x + dx]
                        if cell != '':
                            if cell.isupper() != my_case:
                                board[self.coord.y][self.coord.x] = ''
                                fig = board[self.coord.y + dy][self.coord.x + dx]
                                board[self.coord.y + dy][
                                    self.coord.x + dx] = 'p'
                                if not self.check_to_king(self.color, coord_of_king, board):
                                    self.moves.append(Coord(self.coord.y + dy, self.coord.x + dx))
                                board[self.coord.y + dy][self.coord.x + dx] = fig
                                board[self.coord.y][self.coord.x] = 'p'

                cell = board[self.coord.y + 1][self.coord.x]
                if cell == '':
                    board[self.coord.y][self.coord.x] = ''
                    board[self.coord.y + 1][
                        self.coord.x] = 'p'
                    if not self.check_to_king(self.color, coord_of_king, board):
                        self.moves.append(Coord(self.coord.y + 1, self.coord.x))
                    board[self.coord.y + 1][self.coord.x] = ''
                    board[self.coord.y][self.coord.x] = 'p'

                    if self.coord.y == 1:
                        if board[self.coord.y + 2][self.coord.x] == '':
                            board[self.coord.y][self.coord.x] = ''
                            board[self.coord.y + 2][
                                self.coord.x] = 'p'
                            if not self.check_to_king(self.color, coord_of_king, board):
                                self.moves.append(Coord(self.coord.y + 2, self.coord.x))
                            board[self.coord.y + 2][self.coord.x] = ''
                            board[self.coord.y][self.coord.x] = 'p'

        # black pawn

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
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell.upper() == 'N':
                            return True

        # black pawn
        for dx, dy in ((1, 1), (-1, 1)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'p':
                            return True
        # white pawn
        for dx, dy in ((1, -1), (-1, -1)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.isupper() != my_case:
                        if cell == 'P':
                            return True

        # king
        for dx, dy in ((1, 1), (-1, -1), (-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0)):
            if 0 <= coord_of_king.y + dy < 8 and 0 <= coord_of_king.x + dx < 8:
                cell = board[coord_of_king.y + dy][coord_of_king.x + dx]
                if cell != '':
                    if cell.upper() == 'K':
                        return True

        return False
