from src.Node import Node
from src.chess import Chess
from src.enums import FigureType, Color
from copy import deepcopy


class Tree:
    def __init__(self, chess_object) -> None:
        self.head: Node = Node(chess_object)

    @staticmethod
    def from_type_to_letter(type_of_fig: FigureType, color: Color):
        d = {FigureType.king: 'k', FigureType.queen: 'q', FigureType.rook: 'r', FigureType.knight: 'n',
             FigureType.bishop: 'b', FigureType.pawn: 'p'}
        if color is Color.white:
            return d[type_of_fig].upper()
        else:
            return d[type_of_fig]

    def find_best_move(self, node: Node, deep: int) -> bool:
        # print(deep)
        # print(node.value.position.is_mate)
        if node.value.position.is_mate and node.value.order_of_move == 'b':
            print(1)
            return True
        elif node.value.position.is_mate and node.value.order_of_move == 'w':
            print(2)
            return False
        elif deep == 0:  # с точностью до еденицы
            print(3)
            return False
        else:
            if node.value.order_of_move == 'b':
                figures = node.value.position.black_figures
            else:
                figures = node.value.position.white_figures
            children = []

            for figure in figures:
                for move in figure.moves:
                    board = node.value.board
                    fig = board[move.y][move.x]
                    board[move.y][move.x] = self.from_type_to_letter(figure.type, figure.color)
                    # new_board = deepcopy(board)
                    node.value.position.order_of_move = 'w' if node.value.position.order_of_move == 'b' else 'b'
                    new_fen = node.value.generate_fen()
                    node.value.position.order_of_move = 'w' if node.value.position.order_of_move == 'b' else 'b'


                    board[move.y][move.x] = fig
                    board[figure.coord.y][figure.coord.x] = self.from_type_to_letter(figure.type, figure.color)
                    new_chess = Chess(new_fen)
                    # new_chess.order_of_move = 'w' if new_chess.order_of_move == 'b' else 'b'
                    new_chess.position.generate_general_moves()
                    print(new_chess.position.black_figures[0].moves)
                    print(new_chess.position.is_mate)
                    new_node = Node(new_chess)
                    children.append(self.find_best_move(new_node, deep - 1))

            if node.value.order_of_move == 'b':
                return all(children)
            else:
                return any(children)


if __name__ == '__main__':
    obj = Chess('8/5K1k/8/6R1/8/8/8/8 w - - 0 1')
    obj.position.generate_general_moves()
    tree = Tree(obj)
    print(tree.find_best_move(tree.head, 1))
