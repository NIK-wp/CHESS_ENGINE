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
        pass


