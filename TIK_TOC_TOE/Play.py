import os
import random
import tkinter as tk
import tkinter.messagebox
import functools

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        
        self.the_board = [' '] * 10
        self.player1_marker, self.player2_marker = 'X', 'O'
        self.player1_name, self.player2_name = 'Player X', 'Player O' 
        self.turn = self.choose_first()
        self.game_on = True

        x_position = (self.root.winfo_screenwidth() - 350) // 2
        y_position = (self.root.winfo_screenheight() - 300) // 2
        self.root.geometry(f"350x300+{x_position}+{y_position}")

        self.buttons = []
        for i in range(1, 10):
            row = (i - 1) // 3
            col = (i - 1) % 3
            button = tk.Button(root, text=' ', font=('Helvetica', 28), height=2, width=5,
                               command=functools.partial(self.button_click, position=i))
            button.grid(row=row, column=col)
            self.buttons.append(button)

        # Calculate the position to center the status label
        self.status_label = tk.Label(root, text=f"{self.turn}'s turn", font=('Helvetica', 0))
        self.status_label.grid(row=3, columnspan=3, pady=10)

        self.update_status()

    def choose_first(self):
        choose = random.randint(1, 2)
        return 'Player X' if choose == 1 else 'Player O'

    def update_board(self):
        for i in range(1, 10):
            self.buttons[i - 1].config(text=self.the_board[i])

    def update_status(self):
        self.status_label.config(text=f"{self.turn}'s turn")

    def place_marker(self, position):
        self.the_board[position] = self.player1_marker if self.turn == 'Player X' else self.player2_marker

    def win_check(self):
        mark = self.player1_marker if self.turn == 'Player X' else self.player2_marker

        # Check for win conditions in rows, columns, and diagonals
        for i in range(0, 3):
            if (self.the_board[i] == self.the_board[i + 3] == self.the_board[i + 6] == mark) or \
            (self.the_board[i * 3] == self.the_board[i * 3 + 1] == self.the_board[i * 3 + 2] == mark):
                return True
        if (self.the_board[0] == self.the_board[4] == self.the_board[8] == mark) or \
        (self.the_board[2] == self.the_board[4] == self.the_board[6] == mark):
            return True
        return False

    def full_board_check(self):
        return all(position != ' ' for position in self.the_board[1:])

    def button_click(self, position):
        if self.space_check(position) and self.game_on:
            self.place_marker(position)
            self.update_board()
            if self.win_check():
                self.display_winner()
            elif self.full_board_check():
                self.display_tie()
            else:
                self.turn = 'Player X' if self.turn == 'Player O' else 'Player O'
                self.update_status()


    def space_check(self, position):
        return self.the_board[position] == ' '

    def display_tie(self):
        self.update_board()
        tkinter.messagebox.showinfo("Game Over", "It's a tie!")
        self.root.quit()
    def display_winner(self):
        self.update_board()
        if self.turn == 'Player X':
            winner_name = self.player1_name
        else:
            winner_name = self.player2_name
        tkinter.messagebox.showinfo("Game Over", f"{winner_name} wins!")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()