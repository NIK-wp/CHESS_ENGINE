import hashlib

import pytest

from src.chess import Chess


class TestChess:
    @pytest.mark.parametrize(
        'fen, hash_str, comment',
        [
            ('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1',
             'dfc1b7c4d8f7afd3236c5c97d3e724125302af3390848244d4d99d907f51c9d4', 'StandartPosition'),
            ('8/8/8/8/8/8/8/8 w KQkq - 0 1',
             'abff90966f511af88a411cba93ff4d437275e660340dadef8a501d303d7564b8', 'ZeroPosition')
        ]
    )
    def test_check_attribute_board(self, fen, hash_str, comment):
        fen_of_classical_position = fen
        position = Chess(fen_of_classical_position)
        hash_position = hashlib.sha256(str(position.board).encode()).hexdigest()
        assert hash_position == hash_str, comment
