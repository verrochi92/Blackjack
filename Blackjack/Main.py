# Main.py

# Creates the UI for the Blackjack game
# Also contains some functions that deal with menu options

# By Nick Verrochi
# Last Modified: 5/14/16

# tkinter libraries
from tkinter import *
import tkinter.messagebox as box

from Game import Game

class User:
# used to pass balance by reference

    def __init__(self):
        self.balance = 0

class Main:

    # Functions
    ############################################

    def Play(self, e = None):
    # Launches game
        game = Game(self.window, self.user)

    def Confirm(self, e = None):
    # Prompts for confirmation
        return box.askyesno("Confirmation", "Are you sure?")

    def Quit(self, e = None):
    # Are you sure?
        if self.Confirm():
            self.window.destroy()

    def Reset(self, e = None):
    # Reset balance to 0
        if self.Confirm():
            box.showinfo("Balance Reset", "Your balance is now $0.00")
            self.user.balance = 0

    def Display(self, e = None):
    # Print balance in messagebox
        box.showinfo("Current Balance", "You have a balance of : $%.2f" % self.user.balance)

    # End Functions ############################

    # __init__ - This is what runs the program
    ############################################
    
    def __init__(self):
        # initialize user balance (integer used for accuracy)
        self.user = User()

        # create UI
        self.window = Tk()
        self.window.title("BlackJack!")

        # top menu
        menu = Menu(self.window)
        self.window.config(menu = menu)

        gameMenu = Menu(menu)
        menu.add_cascade(label = "Game", menu = gameMenu)
        gameMenu.add_command(label = "Play the Game", command = self.Play)
        gameMenu.add_separator()
        gameMenu.add_command(label = "Display Available Funds", command = self.Display)
        gameMenu.add_command(label = "Reset Funds to Zero", command = self.Reset)

        menu.add_command(label = "Quit", command = self.Quit)

        # title label
        label = Label(self.window, text = "Welcome to BlackJack!")
        label.pack(side = TOP, padx = 50, pady = 25)

        # frame to hold buttons
        frame = Frame(self.window)
        btPlay = Button(frame, text = "Play the Game", command = self.Play, width = 30)
        btPlay.pack(pady = 3)
        btDisplay = Button(frame, text = "Display Available Funds", command = self.Display, width = 30)
        btDisplay.pack(pady = 3)
        btReset = Button(frame, text = "Reset Funds to Zero", command = self.Reset, width = 30)
        btReset.pack(pady = 3)
        btQuit = Button(frame, text = "Quit", command = self.Quit, width = 30)
        btQuit.pack(pady = 3)

        frame.pack(side = BOTTOM, padx = 20, pady = 10)
        self.window.resizable(0, 0)
        
        # key binding
        self.window.bind("<Return>", self.Play)
        self.window.bind("<Escape>", self.Quit)

        self.window.mainloop()

# to launch
if __name__ == "__main__":
    Main()
