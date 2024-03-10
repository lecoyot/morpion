import random

class Morpion:
    def __init__(self):
        self.board = [["-" for _ in range(3)] for _ in range(3)]
        self.players = ["", ""]
        self.symbols = ["X", "O"]
        self.current_player = 0

    def display_board(self):
        for row in self.board:
            print(" | ".join(row))
        print()

    def add_players(self):
        self.players[0] = input("Player 1, TAPEZ VOTRE PSEUDO: ")
        self.players[1] = input("Player 2, TAPEZ VOTRE PSEUDO: ")

    def switch_player(self):
        self.current_player = 1 - self.current_player

    def make_move(self):
        player = self.players[self.current_player]
        symbol = self.symbols[self.current_player]

        while True:
            try:
                row = int(input(f"{player}, Choisir une ligne (1, 2, 3): ")) - 1
                col = int(input(f"{player}, Choisir une colonne (1, 2, 3): ")) - 1

                if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == "-":
                    self.board[row][col] = symbol
                    break
                else:
                    print("Essayer à nouveau.")
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")

    def check_win(self):
        for i in range(3):
            
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "-":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "-":
                return True

        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "-":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "-":
            return True

        return False

    def check_draw(self):
        return all(cell != "-" for row in self.board for cell in row)

    def play(self):
        self.add_players()
        self.display_board()

        for _ in range(9):  
            self.make_move()
            self.display_board()

            if self.check_win():
                print(f"{self.players[self.current_player]} Félicitations")
                break
            elif self.check_draw():
                print("Match partager!")
                break

            self.switch_player()

if __name__ == "__main__":
    morpion_game = Morpion()
    morpion_game.play()
