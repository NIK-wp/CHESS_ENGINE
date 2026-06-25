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
        all_possible_moves = []
        for white_fig in self.position.white_figures:
            for move in white_fig.moves:
                all_possible_moves.append(move)
        for black_fig in self.position.black_figures:
            for move in black_fig.moves:
                all_possible_moves.append(move)

        print('_ _ _ _ _ _ _ _')
        print()
        for y in range(8):
            for x in range(8):
                if Coord(y, x) in all_possible_moves:
                    print('*', end=' ')
                elif self.board[y][x] != '':
                    print(self.board[y][x], end=' ')
                else:
                    print('-', end=' ')
            print()
        print()
        print('_ _ _ _ _ _ _ _')
        print(self.position.white_figures)
        print(self.position.black_figures)

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
        if len(main_of_fen) > 4:
            self.half_move_clock = int(main_of_fen[4])
        if len(main_of_fen) > 5:
            self.full_move_number = int(main_of_fen[5])

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
        # print(self.order_of_move)
        fen += ' ' + self.position.order_of_move + ' '
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

    def apply_move(self, from_y: int, from_x: int, to_y: int, to_x: int, promotion: str | None = None) -> str:
        moving_piece = self.board[from_y][from_x]
        if not moving_piece:
            raise ValueError('There is no piece on the source square')

        if moving_piece.isupper() != (self.position.order_of_move == 'w'):
            raise ValueError('The selected piece does not belong to the active color')

        legal_move = self._find_legal_move(from_y, from_x, to_y, to_x, promotion)
        if legal_move is None:
            raise ValueError('Illegal move')

        target_piece = self.board[to_y][to_x]
        self._remove_castling_after_move(moving_piece, from_y, from_x, to_y, to_x, target_piece)

        self.board[from_y][from_x] = ''
        is_en_passant = (
                moving_piece.upper() == 'P'
                and self.position.coord_of_en_passant == Coord(to_y, to_x)
                and target_piece == ''
                and from_x != to_x
        )
        if is_en_passant:
            captured_pawn_y = to_y + 1 if moving_piece == 'P' else to_y - 1
            self.board[captured_pawn_y][to_x] = ''

        piece_for_target = getattr(legal_move, 'figure', moving_piece)
        if moving_piece.islower():
            piece_for_target = piece_for_target.lower()
        self.board[to_y][to_x] = piece_for_target

        if moving_piece.upper() == 'K' and abs(to_x - from_x) == 2:
            self._apply_castling_rook_move(from_y, from_x, to_x)

        self.position.coord_of_en_passant = None
        if moving_piece.upper() == 'P' and abs(to_y - from_y) == 2:
            self.position.coord_of_en_passant = Coord((from_y + to_y) // 2, from_x)

        if moving_piece.upper() == 'P' or target_piece or is_en_passant:
            self.half_move_clock = 0
        else:
            self.half_move_clock += 1

        if self.position.order_of_move == 'b':
            self.full_move_number += 1

        self.order_of_move = 'b' if self.position.order_of_move == 'w' else 'w'
        self.position.order_of_move = self.order_of_move
        return self.generate_fen()

    def _find_legal_move(self, from_y: int, from_x: int, to_y: int, to_x: int, promotion: str | None):
        if self.position.order_of_move == 'w':
            figures = self.position.white_figures
        else:
            figures = self.position.black_figures

        for figure in figures:
            if figure.coord == Coord(from_y, from_x):
                if not figure.moves:
                    figure.generate_moves(
                        self.position.coord_of_white_king if self.position.order_of_move == 'w'
                        else self.position.coord_of_black_king,
                        self.position.coord_of_en_passant,
                        self.board,
                        self.position.filling_in_the_castling_parameters(FigureType.king, figure.color),
                        self.position.filling_in_the_castling_parameters(FigureType.queen, figure.color)
                    )
                for move in figure.moves:
                    if move == Coord(to_y, to_x):
                        if promotion and hasattr(move, 'figure') and move.figure.lower() != promotion.lower():
                            continue
                        return move
        return None

    def _remove_castling_after_move(self, moving_piece: str, from_y: int, from_x: int,
                                    to_y: int, to_x: int, target_piece: str) -> None:
        if moving_piece == 'K':
            self.position.castling['K'] = False
            self.position.castling['Q'] = False
        elif moving_piece == 'k':
            self.position.castling['k'] = False
            self.position.castling['q'] = False
        elif moving_piece == 'R' and from_y == 7 and from_x == 0:
            self.position.castling['Q'] = False
        elif moving_piece == 'R' and from_y == 7 and from_x == 7:
            self.position.castling['K'] = False
        elif moving_piece == 'r' and from_y == 0 and from_x == 0:
            self.position.castling['q'] = False
        elif moving_piece == 'r' and from_y == 0 and from_x == 7:
            self.position.castling['k'] = False

        if target_piece == 'R' and to_y == 7 and to_x == 0:
            self.position.castling['Q'] = False
        elif target_piece == 'R' and to_y == 7 and to_x == 7:
            self.position.castling['K'] = False
        elif target_piece == 'r' and to_y == 0 and to_x == 0:
            self.position.castling['q'] = False
        elif target_piece == 'r' and to_y == 0 and to_x == 7:
            self.position.castling['k'] = False

    def _apply_castling_rook_move(self, king_y: int, king_from_x: int, king_to_x: int) -> None:
        if king_to_x > king_from_x:
            rook_from_x = 7
            rook_to_x = king_to_x - 1
        else:
            rook_from_x = 0
            rook_to_x = king_to_x + 1

        self.board[king_y][rook_to_x] = self.board[king_y][rook_from_x]
        self.board[king_y][rook_from_x] = ''

    def get_moves_for_active_color(self) -> dict[str, list]:
        main_color_moves = {}
        if self.order_of_move == 'w':
            for white_fig in self.position.white_figures:
                main_color_moves[f'{white_fig.coord.y},{white_fig.coord.x}'] = []
                for move in white_fig.moves:
                    main_color_moves[f'{white_fig.coord.y},{white_fig.coord.x}'].append(f'{move.y},{move.x}')
        else:
            for black_fig in self.position.black_figures:
                main_color_moves[f'{black_fig.coord.y},{black_fig.coord.x}'] = []
                for move in black_fig.moves:
                    main_color_moves[f'{black_fig.coord.y},{black_fig.coord.x}'].append(f'{move.y},{move.x}')
        return main_color_moves


if __name__ == '__main__':
    fen = '8/k7/8/8/8/4R3/8/5K2 w - - 0 1'
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
