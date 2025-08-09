import pytest

from src.chess import Chess
from src.enums import Color


class TestPosition:
    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/7k/8/8/3K3r/8/8/8 w - - 0 1', Color.white, '1 rook_with_check'),
            ('2r5/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '2 rook_with_check')
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
            ('8/8/8/8/2K1R2r/8/8/8 w - - 0 1', Color.white, '1 rook_without_check'),
            ('8/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '2 rook_without_check'),
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

    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('7b/8/8/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_with_check'),
            ('7b/b7/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_with_check')
        ]
    )
    def test_function_check_to_king_bishop_with_check(self, fen: str, color: Color,
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
            ('7b/8/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_without_check'),
            ('7b/8/5p2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_without_check'),
        ]
    )
    def test_function_check_to_king_bishop_without_check(self, fen: str, color: Color,
                                                         comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/4n3/8/3K4/8/8/8 w - - 0 1 w - - 0 1', Color.white, '1 knight_with_check'),
            ('8/8/8/8/3K4/5n2/8/8 w - - 0 1 w - - 0 1', Color.white, '2 knight_with_check'),
            ('8/8/4N3/8/3k4/8/8/8 w - - 0 1', Color.black, '3 knight_with_check'),
            ('8/8/2N1N3/1N3N2/3K4/1N3n2/2N1N3/8 w - - 0 1', Color.white, '4 knight_with_check')
        ]
    )
    def test_function_check_to_king_knight_with_check(self, fen: str, color: Color,
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
            ('8/8/8/8/3K4/4n3/8/8 w - - 0 1 w - - 0 1', Color.white, '1 knight_without_check'),
            ('8/8/8/8/3K4/8/3n4/8 w - - 0 1 w - - 0 1', Color.white, '2 knight_without_check'),
            ('8/8/3n4/2n1n3/1n1K1n2/2n1n3/3n4/8 w - - 0 1', Color.white, '3 knight_without_check'),
            ('8/8/2N1N3/1N3N2/3K4/1N3N2/2N1N3/8 w - - 0 1', Color.white, '4 knight_without_check')

        ]
    )
    def test_function_check_to_king_knight_without_check(self, fen: str, color: Color,
                                                         comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)

    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/4p3/3K4/8/8/8 w - - 0 1', Color.white, '1 pawn_with_check'),
            ('8/8/8/2p5/3K4/8/8/8 w - - 0 1', Color.white, '2 pawn_with_check'),
        ]
    )
    def test_function_check_to_king_pawn_with_check(self, fen: str, color: Color,
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
            ('8/8/8/3p4/3K4/8/8/8 w - - 0 1', Color.white, '1 pawn_without_check'),
            ('8/8/8/8/3K4/4p3/8/8 w - - 0 1', Color.white, '2 pawn_without_check'),
            ('8/8/8/8/3K4/2P1p3/8/8 w - - 0 1', Color.white, '2 pawn_without_check')
        ]
    )
    def test_function_check_to_king_pawn_without_check(self, fen: str, color: Color,
                                                         comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)

    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/4k3/3K4/8/8/8 w - - 0 1', Color.white, '1 king_with_check'),
            ('8/8/8/4k3/3K4/8/8/8 w - - 0 1', Color.black, '2 king_with_check'),
        ]
    )
    def test_function_check_to_king_with_check(self, fen: str, color: Color,
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
            ('8/8/8/8/3K4/5k2/8/8 w - - 0 1', Color.white, '1 king_without_check'),
            ('8/8/8/8/3K4/5k2/8/8 w - - 0 1', Color.black, '2 king_without_check'),
        ]
    )
    def test_function_check_to_king_without_check(self, fen: str, color: Color,
                                                       comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment
        # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
        # check_board = Chess(fen)
        # check_board.show_board()
        # check_board.position.check_to_king(Color.white)