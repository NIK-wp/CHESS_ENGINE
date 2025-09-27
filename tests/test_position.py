import pytest

from src.chess import Chess
from src.enums import Color
from src.figure import Figure


class TestPosition:
    # fen = '8/8/8/8/2K1p2r/8/8/8 w - - 0 1'
    # check_board = Chess(fen)
    # check_board.show_board()
    # check_board.position.check_to_king(Color.white)
    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/7k/8/8/3K3r/8/8/8 w - - 0 1', Color.white, '1 rook_with_check'),
            ('2r5/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '2 rook_with_check'),
            ('8/8/8/k6R/8/8/8/8 w - - 0 1', Color.black, '3 rook_with_check'),
            ('8/8/8/6kR/8/8/8/8 w - - 0 1', Color.black, '4 rook_with_check'),
            ('k7/8/8/8/8/8/8/R7 w - - 0 1', Color.black, '5 rook_with_check'),
            ('3K4/3r4/8/8/8/8/8/8 w - - 0 1', Color.white, '6 rook_with_check'),
            ('k7/8/8/8/8/8/8/Q7 w - - 0 1', Color.black, '5 rook_with_check queen'),
            ('3K4/3q4/8/8/8/8/8/8 w - - 0 1', Color.white, '6 rook_with_check queen'),
            ('8/8/8/8/K6q/8/8/8 w - - 0 1', Color.white, '7 rook_with_check queen'),
            ('3k4/8/8/8/8/8/8/3Q4 w - - 0 1', Color.black, '8 rook_with_check queen')
        ]
    )
    def test_function_check_to_king_rook_or_queen_with_check(self, fen: str, color: Color,
                                                             comment: str) -> None:
        chess = Chess(fen)
        coord_of_king = chess.position.coord_of_white_king if color is Color.white else chess.position.coord_of_black_king
        assert Figure.check_to_king(color, coord_of_king, chess.position.board), comment

        assert chess.position.check_to_king(color), comment


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/8/2K1R2r/8/8/8 w - - 0 1', Color.white, '1 rook_without_check'),
            ('8/8/8/8/2K1p2r/8/8/8 w - - 0 1', Color.white, '2 rook_without_check'),
            ('8/8/8/8/2K3R1/8/8/8 w - - 0 1', Color.white, '3 rook_without_check'),
            ('8/8/8/8/2k3r1/8/8/8 w - - 0 1', Color.black, '4 rook_without_check'),
            ('8/3k4/8/8/3r4/8/8/3R4 w - - 0 1', Color.black, '5 rook_without_check'),
            ('8/3k4/8/8/3p4/8/8/3R4 w - - 0 1', Color.black, '6 rook_without_check'),
            ('8/8/8/8/2k3q1/8/8/8 w - - 0 1', Color.black, '4 rook_without_check queen'),
            ('8/3k4/8/8/3r4/8/8/3Q4 w - - 0 1', Color.black, '5 rook_without_check queen'),
            ('8/3k4/8/8/3p4/8/8/3Q4 w - - 0 1', Color.black, '6 rook_without_check queen')
        ]
    )
    def test_function_check_to_king_rook_or_queen_without_check(self, fen: str, color: Color,
                                                                comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('7b/8/8/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_with_check'),
            ('7b/b7/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_with_check'),
            ('8/8/8/2k5/8/8/8/6B1 w - - 0 1', Color.black, '3 bishop_with_check'),
            ('5B2/8/8/2k5/8/4p3/8/6B1 w - - 0 1', Color.black, '4 bishop_with_check'),
            ('7q/8/8/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_with_check queen'),
            ('7q/q7/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_with_check queen'),
            ('8/8/8/2k5/8/8/8/6Q1 w - - 0 1', Color.black, '3 bishop_with_check queen'),
            ('5Q2/8/8/2k5/8/4p3/8/6Q1 w - - 0 1', Color.black, '4 bishop_with_check queen')

        ]
    )
    def test_function_check_to_king_bishop_or_queen_with_check(self, fen: str, color: Color,
                                                               comment: str) -> None:
        chess = Chess(fen)

        assert chess.position.check_to_king(color), comment


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('7b/8/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_without_check'),
            ('7b/8/5p2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_without_check'),
            ('5b2/4p3/8/2K5/8/4P3/8/6b1 w - - 0 1', Color.white, '3 bishop_without_check'),
            ('8/8/3k4/8/1p3P2/B7/7B/8 w - - 0 1', Color.black, '4 bishop_without_check'),
            ('7q/8/5P2/8/3K4/8/8/8 w - - 0 1', Color.white, '1 bishop_without_check queen'),
            ('7q/8/5p2/8/3K4/8/8/8 w - - 0 1', Color.white, '2 bishop_without_check queen'),
            ('5q2/4p3/8/2K5/8/4P3/8/6q1 w - - 0 1', Color.white, '3 bishop_without_check queen'),
            ('8/8/3k4/8/1p3P2/q7/7q/8 w - - 0 1', Color.black, '4 bishop_without_check queen'),

        ]
    )
    def test_function_check_to_king_bishop_or_queen_without_check(self, fen: str, color: Color,
                                                                  comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment

    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/4n3/8/3K4/8/8/8 w - - 0 1 w - - 0 1', Color.white, '1 knight_with_check'),
            ('8/8/8/8/3K4/5n2/8/8 w - - 0 1 w - - 0 1', Color.white, '2 knight_with_check'),
            ('8/8/4N3/8/3k4/8/8/8 w - - 0 1', Color.black, '3 knight_with_check'),
            ('8/8/2N1N3/1N3N2/3K4/1N3n2/2N1N3/8 w - - 0 1', Color.white, '4 knight_with_check'),
            ('8/8/2N1N3/1N3N2/3k4/13n2/2N1N3/8 w - - 0 1', Color.black, '4 knight_with_check')
        ]
    )
    def test_function_check_to_king_knight_with_check(self, fen: str, color: Color,
                                                      comment: str) -> None:
        chess = Chess(fen)

        assert chess.position.check_to_king(color), comment


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/8/3K4/4n3/8/8 w - - 0 1 w - - 0 1', Color.white, '1 knight_without_check'),
            ('8/8/8/8/3K4/8/3n4/8 w - - 0 1 w - - 0 1', Color.white, '2 knight_without_check'),
            ('8/8/3n4/2n1n3/1n1K1n2/2n1n3/3n4/8 w - - 0 1', Color.white, '3 knight_without_check'),
            ('8/8/2N1N3/1N3N2/3K4/1N3N2/2N1N3/8 w - - 0 1', Color.white, '4 knight_without_check'),
            ('2N1N3/1N1N1N2/8/1NNkNN2/8/1N1N1N2/2N1N3/8 w - - 0 1', Color.black, '5 knight_without_check')

        ]
    )
    def test_function_check_to_king_knight_without_check(self, fen: str, color: Color,
                                                         comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment


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


    @pytest.mark.parametrize(
        'fen, color, comment',
        [
            ('8/8/8/3p4/3K4/8/8/8 w - - 0 1', Color.white, '1 pawn_without_check'),
            ('8/8/8/8/3K4/4p3/8/8 w - - 0 1', Color.white, '2 pawn_without_check'),
            ('8/8/8/8/3K4/2P1p3/8/8 w - - 0 1', Color.white, '2 pawn_without_check'),
            ('8/8/8/3p4/2pKp3/2ppp3/8/8 w - - 0 1', Color.white, '3 pawn_without_check'),
            ('8/8/8/2PPP3/2PkP3/3P4/8/8 w - - 0 1', Color.black, '4 pawn_without_check')
        ]
    )
    def test_function_check_to_king_pawn_without_check(self, fen: str, color: Color,
                                                       comment: str) -> None:
        chess = Chess(fen)

        assert not chess.position.check_to_king(color), comment


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

