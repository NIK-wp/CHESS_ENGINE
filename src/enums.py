from enum import Enum


class Color(Enum):
    white = 'white'
    black = 'black'


class FigureType(Enum):
    king = 'king'
    queen = 'queen'
    bishop = 'bishop'
    knight = 'knight'
    rook = 'rook'
    pawn = 'pawn'
