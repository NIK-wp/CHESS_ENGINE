import hashlib

from src.coord import Coord
from src.enums import Color, FigureType
from src.figure import Figure
from src.position import Position

"""импорт класса Coord из другого файла"""


class Chess:
    """
    Базовый класс для визуализации и логики шахмат

    """

    def __init__(self, fen: str) -> None:
        """
        Args:
            board: двумерный список для представления шахматной доски

            order_of_move: Отслеживает,чей ход ('white' или 'black')

            castling: Словарь для отслеживания наличия рокировок

            full_move_number: Подсчитывает общее количество ходов в игре

            halfmove_clock: Подсчитывает количество ходов без движения пешек в соответствии с правилом о 50 ходах

            coord_of_en_passant: отслеживает координату хода пешки на 2 клетки вперёд
        """
        self.board: list[list[str]] = [['' for _ in range(8)] for _ in range(8)]
        self.order_of_move: str = 'w'
        self.castling: dict = {}
        self.full_move_number: int = 0
        self.halfmove_clock: int = 0
        self.coord_of_en_passant: Coord | None = None
        self.position: Position = Position()

        self.parse_fen(fen)

    def show_board(self) -> None:
        """Визуализация шахматной доски."""
        print('_ _ _ _ _ _ _ _')
        for line in self.board:
            for symbol in line:
                if symbol:
                    print(symbol, end=' ')
                else:
                    print('-', end=' ')
            print()

        print('_ _ _ _ _ _ _ _')

    def parse_fen(self, fen: str) -> None:
        """Анализ строк FEN Forsyth–Edwards Notation"""

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
    fen = '8/8/8/8/8/8/8/8 w KQkq - 0 1'
    check_board = Chess(fen)
    check_board.show_board()

    str_board = str(check_board.board)
    byte_str = str_board.encode()
    hash_board = hashlib.sha256(byte_str)
    str_hash = hash_board.hexdigest()
    print(str_hash)




    # # king + pawns
    # chess_game = Chess('8/8/4p3/3K4/2P5/8/8/8 w - - 0 1')
    # chess_game.generate_moves()
    # chess_game.show_moves()
    # chess_game = Chess('8/8/4p3/3K4/2P5/8/8/8 w - - 0 1')
    # chess_game.show_board()
