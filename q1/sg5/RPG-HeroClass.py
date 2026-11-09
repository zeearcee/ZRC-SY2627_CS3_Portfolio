class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        pass

    def take_damage(self, amount):
        self.hp -= amount
        pass

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

if arthur.hp < 100 and arthur.hp > 0: # assuming that original hp is ahealth.
    print(f"{arthur.name} has reduced HP to {arthur.hp}!")
elif arthur.hp <= 0:
    print(f"{arthur.name} has been defeated!")
elif arthur.hp == 100: # Assuming that original hp is 100, and current hp is also 100.
    print(f"{arthur.name} has {arthur.hp} HP remaining!")

if morgana.hp < 100 and morgana.hp > 0: # assuming that original hp is 100.
    print(f"{morgana.name} has reduced HP to {morgana.hp}!")
elif morgana.hp <= 0:
    print(f"{morgana.name} has been defeated!")
elif morgana.hp == 100: # Assuming that original hp is 100, and current hp is also 100.
    print(f"{morgana.name} has {morgana.hp} HP remaining!")