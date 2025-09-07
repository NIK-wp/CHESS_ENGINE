import tkinter as tk
from tkinter import font

from src.chess import Chess


class ChessGUI:
    def __init__(self, chess):
        self.chess = chess
        self.root = tk.Tk()
        self.root.title("Chess GUI")

        self.cell_size = 60
        self.canvas = tk.Canvas(
            self.root,
            width=self.cell_size * 8,
            height=self.cell_size * 8
        )
        self.canvas.pack()

        self.font = font.Font(size=24, weight="bold")

        self.selected_figure = None
        self.highlighted_moves = []

        self.draw_board()
        self.draw_pieces()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                color = "#EEEED2" if (row + col) % 2 == 0 else "#769656"
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

    def draw_pieces(self):
        for row in range(8):
            for col in range(8):
                piece = self.chess.board[row][col]
                if piece != "":
                    x = col * self.cell_size + self.cell_size // 2
                    y = row * self.cell_size + self.cell_size // 2
                    self.canvas.create_text(
                        x, y,
                        text=piece,
                        font=self.font,
                        fill="black" if piece.islower() else "white"
                    )

    def draw_highlights(self):
        for move in self.highlighted_moves:
            x = move.x * self.cell_size + self.cell_size // 2
            y = move.y * self.cell_size + self.cell_size // 2
            self.canvas.create_oval(
                x - 8, y - 8, x + 8, y + 8,
                fill="red", outline=""
            )

    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        clicked_piece = None
        for fig in self.chess.position.white_figures + self.chess.position.black_figures:
            if fig.coord.x == col and fig.coord.y == row:
                clicked_piece = fig
                break

        if clicked_piece:
            self.selected_figure = clicked_piece
            self.highlighted_moves = clicked_piece.moves
        else:
            self.selected_figure = None
            self.highlighted_moves = []


        self.draw_board()
        self.draw_pieces()
        self.draw_highlights()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    fen = "8/6k1/8/3Q4/8/8/1K6/8 w - - 0 1"
    chess = Chess(fen)
    chess.position.generate_general_moves()
    gui = ChessGUI(chess)
    gui.run()
