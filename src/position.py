from src.coord import Coord
from src.figure import Figure


class Position:
    def __init__(self) -> None:
        self.cord_of_white_king: Coord | None = None
        self.cord_of_black_king: Coord | None = None
        self.white_figures: list[Figure] = []
        self.black_figures: list[Figure] = []

    def check_to_king(self) -> bool:
        pass

    def past_pawn(self) -> bool:
        pass

