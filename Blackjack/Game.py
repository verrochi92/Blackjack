# Game.py

# Game class
# Contains functions to handle game logic
# Uses a modal window to display game

# By Nick Verrochi
# Last Modified: 5/14/16

#tkinter libraries
from tkinter import *
import tkinter.messagebox as box

import random

from Card import Card

class Game:
    
    def __init__(self, master, user):
    # Generates UI in modal window then starts the game
        self.user = user
        self.BuildDeck(); # creates member 'self.deck', a list of Cards

        # window setup
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Game")
        self.window.transient(master)
        self.window.grab_set()
        self.window.focus_set()

        # Top Label
        self.label = Label(self.window, text = "Please hit \"Deal\" to begin...")
        self.label.pack(side = TOP, padx = 10, pady = 10)

        # Listbox
        listFrame = Frame(self.window)
        scrollBar = Scrollbar(listFrame)
        self.listBox = Listbox(listFrame, selectmode = SINGLE) # selections not actually used

        scrollBar.pack(side = RIGHT, fill = Y)
        scrollBar.config(command = self.listBox.yview)
        self.listBox.pack(side = LEFT, fill = Y)
        self.listBox.config(yscrollcommand = scrollBar.set)
        listFrame.pack(side = TOP, padx = 20, pady = 10)

        #Buttons
        buttonFrame = Frame(self.window)
        self.btnDeal = Button(buttonFrame, text = "Deal", command = self.Deal, width = 30)
        self.btnHit = Button(buttonFrame, text = "Hit Me!", command = self.Hit, width = 30)

        self.btnDeal.pack(side = TOP, padx = 20, pady = 5)
        self.btnHit.pack(side = TOP, padx = 20, pady = 5)
        buttonFrame.pack(side = BOTTOM, padx = 20, pady = 10)
        self.btnHit.configure(state = DISABLED)

        self.window.bind("<Return>", self.Deal)
        self.window.bind("<Escape>", self.window.destroy)
    #end function __init__

    def Deal(self, e = None):
    # Deals two cards and checks for win
    # Switches buttons if game continues
        self.hand = []

        self.hand.append(self.GetCard())
        self.hand.append(self.GetCard())

        self.listBox.insert(END, self.hand[0].name)
        self.listBox.insert(END, self.hand[1].name)

        self.btnDeal.configure(state = DISABLED)
        self.btnHit.configure(state = NORMAL)
        self.window.bind("<Return>", self.Hit)

        self.Check()
    #end function Deal

    def Hit(self, e = None):
    # Deals a single card and checks for a win
        card = self.GetCard()
        self.hand.append(card)
        self.listBox.insert(END, card.name)

        self.Check()
    #end function Hit

    def GetCard(self):
    # Gets a random card, only used to shorten syntax
        return self.deck.pop(random.randint(0, len(self.deck) - 1))
    #end function GetCard()

    def BuildDeck(self):
    # Builds up deck as a list of Card objects
        self.deck = []
        cardString = ""
        suitString = ""
        value = 0
            
        for i in range(13): # 13 cards
            if i == 0:
                cardString = "Ace"
                value = 11
            elif i >= 10:
                if (i == 10): cardString = "Jack"
                if (i == 11): cardString = "Queen"
                if (i == 12): cardString = "King"
                value = 10
            else:
                cardString = str(i + 1)
                value = i + 1

            for j in range(4): # 4 suits
                if j == 0: suitString = " of Spades"
                if j == 1: suitString = " of Clubs"
                if j == 2: suitString = " of Hearts"
                if j == 3: suitString = " of Diamonds"
                self.deck.append(Card(cardString + suitString, value))
            #end for
        #end for
    #end function BuildDeck

    def Check(self):
    # Checks for a win or loss
        total = 0

        for card in self.hand:
            if card.value == 11 and total + card.value > 21:
                card.Switch() 
            total += card.value

        self.label.configure(text = "Total = %d" % total)

        if total > 21:
            if self.hand[0].value == 11 or self.hand[1].value == 11:
                self.hand[0].Switch()
                self.hand[1].Switch()
                self.Check()
                total = 0
            if (total > 21):
                self.user.balance -= 50
                if (self.user.balance <= -1000):
                    box.showinfo("Game Over", "You can't bet anymore! The game is over!")
                    self.window.destroy()
                    self.master.destroy()
                else:
                    box.showinfo("Loss", "You lose!")
                    self.window.destroy()
        elif total == 21:
            self.user.balance += 100
            box.showinfo("Win", "You won!")
            self.window.destroy()
    #end function Check
