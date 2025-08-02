import pytest

from src.chess import Chess
from src.enums import Color


class TestPosition:
    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/7k/8/8/3K3r/8/8/8 w - - 0 1', Color.white, '1 test True'),
            ('2r5/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '4 test True')
        ]
    )
    def test_function_check_to_king_rook_with_check(self, fen: str, color: Color,
                                                    comment: str) -> None:
        chess = Chess(fen)

        assert chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)

    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/8/2K1R2r/8/8/8 w - - 0 1', Color.white, '2 test False'),
            ('8/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '3 test False'),
        ]
    )
    def test_function_check_to_king_rook_without_check(self, fen: str, color: Color,
                                                       comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)
