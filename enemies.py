import random

# Different enemies the player can encounter
class Goblin:
    def __init__(self):
        self.name = "goblin"
        self.attack = 10

class Skeleton:
    def __init__(self):
        self.name = 'skeleton'
        self.attack = 15

class Slime:
    def __init__(self):
        self.name = 'slime'
        # Add a little bit of randomness; Makes this monster more dangerous
        self.attack = random.randint(10, 20)

class DemonKing:
    def __init__(self):
        self.name = 'demon king'
        self.attack = 50