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
             'abff90966f511af88a411cba93ff4d437275e660340dadef8a501d303d7564b8', 'ZeroPosition'),
            ('r1bqkb1r/pppp1ppp/2n2n2/4p3/4P3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 0 1',
             '56a3ae828a9b1f72952d2bfd2083113aae23e6de42a7c6817a54d8ad1ec4eefc', 'DefendOfTwoKnights'),
            ('r1bqkbnr/pp1ppppp/2n5/1Bp5/4P3/8/PPPP1PPP/RNBQK1NR w KQkq - 0 1',
             'db0842e770691ff9c8eaf8d6db2b8e1fec5e23e614d21677249cbeff19ec3f2c', 'SicilianDefense'),
            ('r1bqkbnr/pp1npppp/2p5/8/3PN3/8/PPP2PPP/R1BQKBNR w KQkq - 0 1',
             'ac67413fc52e84ce7b5eb6e2cad9da1b84ed4b6e5c6f302921013246e1a122df', 'Caro-CanDefense'),
            ('r1bqkb1r/pppp1ppp/2n2n2/4N3/4P3/2N5/PPPP1PPP/R1BQKB1R b KQkq - 0 1',
             'ce8cf1592df24e9612eccc5d1006519261d54ee87f59dcc4cc5e6216452e1c8a', 'FourKnightsDefense')
        ]
    )
    def test_check_attribute_board(self, fen, hash_str, comment):
        fen_of_classical_position = fen
        position = Chess(fen_of_classical_position)
        hash_position = hashlib.sha256(str(position.board).encode()).hexdigest()
        assert hash_position == hash_str, comment
