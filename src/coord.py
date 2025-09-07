"""Модуль, который содержит класс Coord(Реализация шахматных координат)."""


class Coord:
    """Реализация шахматных координат."""

    def __init__(self, y: int, x: int) -> None:
        """Заполняет поля объекта.

        Args:
            x(int): Горизонтальная координата(Символьная);
            y(int): Вертикальная координата(Числовая);
        """
        self.x: int = x
        self.y: int = y
        self.valid: bool = False  # todo athtomatic check

    def check_valid(self) -> bool:
        pass

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'

    def __eq__(self, other: 'Coord') -> bool:
        return self.x == other.x and self.y == other.y


class CoordWithTransform(Coord):
    def __init__(self, y: int, x: int, figure: str) -> None:
        super().__init__(y, x)
        self.figure: str = figure

    def __repr__(self) -> str:
        return f'{self.figure}({self.x}, {self.y})'
