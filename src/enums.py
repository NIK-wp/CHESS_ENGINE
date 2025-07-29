"""Модуль, который содержит перечисления Color, FigureType."""

from enum import Enum


class Color(Enum):
    """Перечисление, которое содержит константы для реализация цветов в игре."""
    white = 'white'
    black = 'black'


class FigureType(Enum):
    """Перечисление, которое содержит константы для реализации типов фигур в игре."""
    king = 'king'
    queen = 'queen'
    bishop = 'bishop'
    knight = 'knight'
    rook = 'rook'
    pawn = 'pawn'
