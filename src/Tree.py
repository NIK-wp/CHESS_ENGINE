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
        if node.value.position.is_mate and node.value.order_of_move == 'b':
            return True
        elif node.value.position.is_mate and node.value.order_of_move == 'w':
            return False
        elif deep == 0:  # с точностью до еденицы
            return False
        else:
            if node.value.order_of_move == 'b':
                figures = node.value.position.black_figures
            else:
                figures = node.value.position.white_figures
            children = []
            state_order = node.value.position.order_of_move
            for figure in figures:
                for move in figure.moves:
                    board = node.value.board
                    fig = board[move.y][move.x]
                    board[move.y][move.x] = self.from_type_to_letter(figure.type, figure.color)
                    node.value.position.order_of_move = 'b' if state_order == 'w' else 'w'
                    new_fen = node.value.generate_fen()
                    node.value.position.order_of_move = state_order
                    board[move.y][move.x] = fig
                    board[figure.coord.y][figure.coord.x] = self.from_type_to_letter(figure.type, figure.color)
                    new_chess = Chess(new_fen)
                    new_chess.position.generate_general_moves()
                    new_node = Node(new_chess)
                    children.append(self.find_best_move(new_node, deep - 1))

            if node.value.order_of_move == 'b':
                return all(children)
            else:
                return any(children)


if __name__ == '__main__':
    obj = Chess('8/4K2k/8/4R3/8/8/8/8 w - - 0 1') # Нет мата за 3 хода
    obj.position.generate_general_moves()
    tree = Tree(obj)
    print(tree.find_best_move(tree.head, 2))
    obj = Chess('8/5K1k/5R2/8/8/8/8/8 w - - 0 1') # Есть мат за 3 хода
    obj.position.generate_general_moves()
    tree = Tree(obj)
    print(tree.find_best_move(tree.head, 2))
    obj = Chess('8/4K1k1/8/5R2/8/8/8/8 w - - 0 1') # Есть мат за 5 ходов
    obj.position.generate_general_moves()
    tree = Tree(obj)
    print(tree.find_best_move(tree.head, 4))
