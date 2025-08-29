"""Модуль, содержащий реализацию класса Chess."""

import hashlib

from src.coord import Coord
from src.enums import Color, FigureType
from src.figure import Figure
from src.position import Position


class Chess:
    """Базовый класс для визуализации и логики шахмат."""

    def __init__(self, fen: str) -> None:
        """Иницилизирует поля класса.

        Args:
            fen(str) : Нотация Форсайта — Эдвардса. Строка, которая кодирует позицию на доске.
        """
        self.board: list[list[str]] = [['' for _ in range(8)] for _ in range(8)]
        self.order_of_move: str = 'w'
        self.castling: dict = {}
        self.full_move_number: int = 0
        self.half_move_clock: int = 0
        self.coord_of_en_passant: Coord | None = None
        self.position: Position = Position()
        self.parse_fen(fen)
        self.position.board = self.board

    def show_board(self) -> None:
        """Визуализация шахматной доски."""
        print('_ _ _ _ _ _ _ _')
        print()
        for line in self.board:
            for symbol in line:
                if symbol:
                    print(symbol, end=' ')
                else:
                    print('-', end=' ')
            print()
        print()
        print('_ _ _ _ _ _ _ _')

    def show_moves(self) -> None:
        all_white_possible_moves = []
        for white_fig in self.position.white_figures:
            for move in white_fig.moves:
                all_white_possible_moves.append(move)
        for black_fig in self.position.black_figures:
            for move in black_fig.moves:
                all_white_possible_moves.append(move)

        print('_ _ _ _ _ _ _ _')
        print()
        for y in range(8):
            for x in range(8):
                if Coord(y, x) in all_white_possible_moves:
                    print('*', end=' ')
                elif self.board[y][x] != '':
                    print(self.board[y][x], end=' ')
                else:
                    print('-', end=' ')
            print()
        print()
        print('_ _ _ _ _ _ _ _')

    def parse_fen(self, fen: str) -> None:
        """Парсинг строки FEN Forsyth–Edwards Notation и заполнение доски.

        Args:
            fen(str): Нотация Форсайта — Эдвардса. Строка, которая кодирует позицию на доске.
        """
        main_of_fen = fen.split()
        board_of_fen = main_of_fen[0].split('/')
        for i in range(len(self.board)):
            for j in range(8):
                if board_of_fen[i] == '8':
                    break
                else:
                    j1 = j
                    for f in range(len(board_of_fen[i])):
                        if board_of_fen[i][f] not in '01234567':
                            self.board[i][j1] = board_of_fen[i][f]
                            if self.board[i][j1].isupper():
                                if self.board[i][j1] == 'K':
                                    self.position.cord_of_white_king = Coord(i, j1)
                                self.position.white_figures.append(Figure(
                                    self.from_symbol_to_figure_type(self.board[i][j1]), Color.white, Coord(i, j1)))
                            else:
                                if self.board[i][j1] == 'k':
                                    self.position.cord_of_black_king = Coord(i, j1)
                                self.position.black_figures.append(
                                    Figure(self.from_symbol_to_figure_type(self.board[i][j1]), Color.black,
                                           Coord(i, j1)))
                            j1 += 1
                        else:
                            j1 += int(board_of_fen[i][f])
                    break

    @staticmethod
    def from_symbol_to_figure_type(string: str) -> FigureType:
        transformator = {'K': FigureType.king, 'k': FigureType.king, 'Q': FigureType.queen, 'q': FigureType.queen,
                         'B': FigureType.bishop, 'b': FigureType.bishop, 'N': FigureType.knight, 'n': FigureType.knight,
                         'R': FigureType.rook, 'r': FigureType.rook, 'P': FigureType.pawn, 'p': FigureType.pawn}
        return transformator[string]


if __name__ == '__main__':
    fen = '8/5k2/8/8/3Q4/8/8/3K4 w - - 0 1'
    check_board = Chess(fen)
    check_board.position.generate_general_moves()
    check_board.show_moves()
