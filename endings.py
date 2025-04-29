
# Contains all the different endings
# Official branches to these endings will be included in main.py
class Ending:
    def game_over(self):
        print("You have been killed.")

    def slay_demon_king(self):
        print('\n=== The Hero ===\n')
        print("You have slayed the Demon King and rescued the princess. The Demon King's forces have retreated and the Kingdom is saved!")

    def convert_demon_king(self):
        print('\n=== Peace Between Us ===\n')
        print("You have successfully persuaded the Demon King to make peace with the Kingdom. Humankind and Demonkind now live peacefully together.")

    def too_late(self):
        print('\n=== Too Late ===\n')
        print("You were too late to save the princess. She was transformed into the Demon Queen.")

    def false_knight(self):
        print('\n=== The Dark Side ===')
        print("Your willpower was waning, and the Demon King took advantage and converted you to his ranks. Having lost their protector, the Kingdom has fallen.")

    def secret_ending(self):
        print('\n=== The New King ===')
        print('You have slayed the Demon King and took control of his powers. You are now the new king of the monsters.')