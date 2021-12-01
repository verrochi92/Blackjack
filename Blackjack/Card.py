# Card class

# Stores card name and value

# By Nick Verrochi
# Last Modified: 5/14/16

class Card:
    def __init__(self, name = "", value = 0):
        self.name = name
        self.value = value

    def Switch(self):
    # switches value of aces from 11 to 1
    # won't do anything to other cards
    # only do if total hand value over 21!
        if self.value == 11:
            self.value = 1
