class Warrior():
    def special_move(self):
        print("Warrior swings a mighty sword!")

class Mage():
    def special_move(self):
        print("Mage casts a powerfull spell!")

class Archer():
    def special_move(self):
        print("Archer shoots a precise arrow!")

def perform_move(character):
    character.special_move()

warrior = Warrior()
mage = Mage()
archer = Archer()

perform_move(warrior)
perform_move(mage)
perform_move(archer)
