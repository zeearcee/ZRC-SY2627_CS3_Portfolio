class HealthPotion():
    def use(self):
        print("You regained 50 HP!")

class ManaPotion():
    def use(self):
        print("You regained 30 MP!")

class SpeedBoost():
    def use(self):
        print("Your speed has increased for 10 seconds!")

def apply_item(item):
    item.use()

health_potion = HealthPotion()
mana_potion = ManaPotion()
speed_boost = SpeedBoost()

apply_item(health_potion)  
apply_item(mana_potion)
apply_item(speed_boost)
