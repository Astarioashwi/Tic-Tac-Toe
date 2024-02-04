import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "," "]
    
    def display(self):
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        
        if self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        
        if self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        
        if self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        
        if self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True

        if self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        
        if self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True
        
        if self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        
        return False
    
    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells ==9:
            return True
        else:
            return False


    def reset(self):
        self.cells = []
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "," "]


board = Board()

def print_header():
    print("Welcome to Tic-Tac-Toe \n" )

def refresh_screen():
    #clear Screen
    os.system("clear")

    #Print the header 
    print_header()

    #Show the board
    board.display()

while True:
    #Refresh Screen
    refresh_screen()

    #Get_X_input
    x_choice = int(input("X "))
    #x_choice = int(input("\n X) Please choose 1 - 9. >"))

    #Update board
    board.update_cell(x_choice, "X")

    #Refresh Screen
    refresh_screen()

    #Check for an X win
    if board.is_winner("X"):
        print (" \n X wins!\n")
        play_again = input("Would you like to play again? (Y/N)> ")
        if play_again == "Y" or play_again == "y" :
            board.reset()
            continue
        else:
            break
    #Check for a tie
    if board.is_tie():
        print (" \n Tie Game!\n")
        play_again = input("Would you like to play again? (Y/N)> ")
        if play_again == "Y" or play_again == "y" :
            board.reset()
            continue
        else:
            break

    #Get_O_input
    o_choice = int(input("O "))
    #x_choice = int(input("\n O) Please choose 1 - 9. >"))

    #Update board
    board.update_cell(o_choice, "O")

    #Check for an O win
    if board.is_winner("O"):
        print (" \n O wins!\n")
        play_again = input("Would you like to play again? (Y/N)> ")
        if play_again == "Y" or play_again == "y" :
            board.reset()
            continue
        else:
            break