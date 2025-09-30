"""Модуль, содержащий реализацию класса Chess."""

# import hashlib

from src.coord import Coord
from src.enums import Color, FigureType
from src.figure import Figure
from src.position import Position


class Chess:
    """Базовый класс для визуализации и логики шахмат."""

    def __init__(self, fen: str = None) -> None:
        """Иницилизирует поля класса.

        Args:
            fen(str) : Нотация Форсайта — Эдвардса. Строка, которая кодирует позицию на доске.
        """
        self.board: list[list[str]] = [['' for _ in range(8)] for _ in range(8)]
        self.order_of_move: str = 'w'
        self.full_move_number: int = 1
        self.half_move_clock: int = 0
        self.position: Position = Position()

        if fen:
            self.parse_fen(fen)
            self.position.board = self.board
            self.position.order_of_move = self.order_of_move

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
        if main_of_fen[1] != '-':
            self.order_of_move = main_of_fen[1]
        if main_of_fen[2] != '-':
            for letter in main_of_fen[2]:
                self.position.castling[letter] = True
        if main_of_fen[3] != '-':
            print(main_of_fen)
            self.position.coord_of_en_passant = Coord(7 - int(main_of_fen[3][1]) + 1,
                                                      self.from_letter_to_coord_type(main_of_fen[3][0]))


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
                                    self.position.coord_of_white_king = Coord(i, j1)
                                self.position.white_figures.append(Figure(
                                    self.from_symbol_to_figure_type(self.board[i][j1]), Color.white, Coord(i, j1)))
                            else:
                                if self.board[i][j1] == 'k':
                                    self.position.coord_of_black_king = Coord(i, j1)
                                self.position.black_figures.append(
                                    Figure(self.from_symbol_to_figure_type(self.board[i][j1]), Color.black,
                                           Coord(i, j1)))
                            j1 += 1
                        else:
                            j1 += int(board_of_fen[i][f])
                    break

    def generate_fen(self) -> str:
        fen = ''
        counter = 0
        for line in self.board:
            for cell in line:
                if cell != '':
                    if counter == 0:
                        fen += cell
                    else:
                        fen += str(counter) + cell
                    counter = 0
                else:
                    counter += 1
            if counter != 0:
                fen += str(counter)
            fen += '/'
            counter = 0
        fen = fen[:-1]
        fen += ' ' + self.order_of_move + ' '
        flug = ''
        for k in self.position.castling.keys():
            if self.position.castling[k]:
                flug += k
        if flug:
            fen += flug
        else:
            fen += '-'

        if self.position.coord_of_en_passant:
            fen += f' {self.from_coord_type_to_letter(self.position.coord_of_en_passant.x)}{8 - self.position.coord_of_en_passant.y}'
        else:
            fen += ' -'
        fen += f' {self.half_move_clock} '
        fen += f'{self.full_move_number}'

        return fen

    @staticmethod
    def from_symbol_to_figure_type(string: str) -> FigureType:
        transformator = {'K': FigureType.king, 'k': FigureType.king, 'Q': FigureType.queen, 'q': FigureType.queen,
                         'B': FigureType.bishop, 'b': FigureType.bishop, 'N': FigureType.knight, 'n': FigureType.knight,
                         'R': FigureType.rook, 'r': FigureType.rook, 'P': FigureType.pawn, 'p': FigureType.pawn}
        return transformator[string]

    def from_letter_to_coord_type(self, letter: str) -> int:
        transformator = {
            'a': 0, 'b': 1, 'c': 2, 'd': 3,
            'e': 4, 'f': 5, 'g': 6, 'h': 7
        }
        return transformator[letter]

    def from_coord_type_to_letter(self, coord: int) -> str:
        transformator = {
            0: 'a', 1: 'b', 2: 'c', 3: 'd',
            4: 'e', 5: 'f', 6: 'g', 7: 'h'
        }
        return transformator[coord]


if __name__ == '__main__':
    fen = '8/5K1k/8/7R/8/8/8/8 b - - 0 1'
    check_board = Chess(fen)
    check_board.position.generate_general_moves()
    check_board.show_moves()
    print(check_board.position.is_mate)

# Start Position(white) - 2.315733699972043
# Start Position(black) - 2.372777100012172
# Middle-game('rnbqkb1r/pp2pppp/5n2/3p4/2PP4/2N5/PP3PPP/R1BQKBNR w KQkq - 0 1') - 3.8795937999966554
# Middle-game('rnbqkb1r/pp2pppp/5n2/3p4/2PP4/2N5/PP3PPP/R1BQKBNR b KQkq - 0 1') - 3.8126058999914676
# The endgame('8/8/8/5PK1/8/k7/8/3r4 w - - 0 1') - 0.9383183000027202
# The endgame('8/8/8/5PK1/8/k7/8/3r4 b - - 0 1') - 0.9392350999987684
