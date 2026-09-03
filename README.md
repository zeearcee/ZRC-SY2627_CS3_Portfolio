
class Hero:
    def __init__(self, name, hp):
       self.name = name
       self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

maria = Hero("Maria", 100)
cocoraz = Hero("Cocoraz", 100)
maria.take_damage(10)

print(maria.name, maria.hp)     # Expected: 90
print(cocoraz.name, cocoraz.hp)    # Expected: 100

#this is pisay
