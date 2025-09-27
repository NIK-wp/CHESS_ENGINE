from src.Node import Node
from src.chess import Chess


class Tree:
    def __init__(self, chess_object) -> None:
        self.head: Node = Node(chess_object)

    def find_best_move(self, node: Node, deep: int) -> bool:
        if node.value.position.is_mate and node.value.order_of_move == 'b':
            return True
        elif node.value.position.is_mate and node.value.order_of_move == 'w':
            return False
        elif deep == 0:  # с точностью до еденицы
            return False
        else:
            pass


if __name__ == '__main__':
    obj = Chess('8/5K1k/5R2/8/8/8/8/8 b - - 0 1')
    tree = Tree(obj)
    print(tree.find_best_move(tree.head, 3))
