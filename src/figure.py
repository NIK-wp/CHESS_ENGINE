from src.coord import Coord
from src.enums import Color, FigureType


class Figure:
    def __init__(self, type_of_figure: FigureType, color: Color, coord: Coord) -> None:
        self.color: Color = color
        self.type: FigureType = type_of_figure
        self.coord: Coord = coord
        self.moves: list = []

    def generate_moves(self, cord_of_king: Coord, board: list[list[str]]) -> None:
        pass


