class Coord:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        self.valid: bool = False  # todo athtomatic check

    def check_valid(self) -> bool:
        pass

