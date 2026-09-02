class Hero:
    def __init__(self, name, hp):
       self.name = name
       self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"Arthurs.HP = {arthur hp}")    
print(f"Morganas.HP = {morgana hp}")    

