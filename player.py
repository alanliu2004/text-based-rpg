class Player:
    # Default Stats
    def __init__(self):
        self.name = ''
        self.origin = ''
        self.max_health = 100
        self.health = 100
        self.demon_knowledge = False
        self.time = 0

    # Lets the user select the difficulty
    def origin_selection(self):
        selection = input("Choose between Easy (Knight) or Hard (Peasant):\n")
        if selection.lower() == 'easy':
            self.origin = 'Knight'
            self.max_health = 150
            self.heal()
        elif selection.lower() == 'hard':
            self.origin = 'Peasant'
        else:
            print("Invalid Choice. Try Again.")
            self.origin_selection()

    def player_name(self):
        name = input(f"You remembered that you were a {self.origin}, and your name was: ")
        self.name = name.upper()

    def player_health(self):
        print(f'Health: {self.health}\n')

    # Mechanic to heal the player to full HP
    def heal(self):
        self.health = self.max_health
    # Decrease Health
    def health_decrease(self, amount):
        self.health -= amount
        print(f'Your health is now: {self.health}.')

    # Increase health
    def health_increase(self, amount):
        self.health += amount
        if self.health >= self.max_health:
            self.health = self.max_health
        print(f'Your health is now: {self.health}.')

    # Increases Timer
    def timer_increase(self):
        self.time += 5

    # Decreases Timer
    def timer_decrease(self):
        self.time -= 5

    # Increase Max Health
    def max_health_increase(self, amount):
        self.max_health += amount
        print(f'Your max health is now {self.max_health}.')

class Morality:
    def __init__(self):
        self.good_evil_compass = 0
    # System where at the end of the game, it will state how good or how evil the user is
    def karma(self, alignment):
        if alignment.lower() == 'evil':
            self.good_evil_compass -= 5
        elif alignment.lower() == 'good':
            self.good_evil_compass += 5
        else:
            self.good_evil_compass = self.good_evil_compass

    def display(self):
        print(f'Your moral compass score is {self.good_evil_compass}. Neutral is 0.')


