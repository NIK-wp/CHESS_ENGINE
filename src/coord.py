"""Модуль, который содержит класс Coord(Реализация шахматных координат)."""


class Coord:
    """Реализация шахматных координат."""

    def __init__(self, x: int, y: int) -> None:
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
