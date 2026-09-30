import time
class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(f"{self.name}: Attack!")
        time.sleep(1)
        amount = self.damage
        zombie.take_damage(amount)

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name}: Im being turn into a salad!")

class Zombie:
    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        print("Zombie: *Walks one tile closer*")
        self.distance -= 1

    def attack(self, plant):
        print(f"Zombie: Attacks {plant.name}")
        print("Zombie: Yum yum yum, in my tum tum tum!")
        time.sleep(1)
        amount = self.damage
        plant.take_damage(amount)

    def take_damage(self, amount):
        self.health -= amount
        print("Zombie: Ow!")

bonk_choy = Plant("Bonk Choy", 100, 25)
snapdragon = Plant("Snapdragon", 150, 40)
zombie = Zombie("Conehead", 300, 50, 5)

turn = 0

while zombie.health > 0:




    if zombie.distance < 1:
        if bonk_choy.health < 1: 
            time.sleep(1)
            zombie.attack(snapdragon)
            time.sleep(1)
            snapdragon.attack(zombie)
            turn += 1
        else:
            time.sleep(1)
            zombie.attack(bonk_choy)
            if turn % 2 == 0:
                time.sleep(1)
                bonk_choy.attack(zombie)
                turn += 1
            elif turn % 2 == 1:
                time.sleep(1)
                snapdragon.attack(zombie)
                turn += 1


    elif zombie.distance > 0:
        if turn % 2 == 0:
            time.sleep(1)
            bonk_choy.attack(zombie)
        elif turn % 2 == 1:
            time.sleep(1)
            snapdragon.attack(zombie)
        time.sleep(1)
        zombie.move()
        turn = turn + 1

    time.sleep(1)
    print(f"Snapdragon Health: {snapdragon.health}")
    time.sleep(1)
    print(f"Bonk Choy Health: {bonk_choy.health}")

    if snapdragon.health <= 0:
        print("Second Plant Dead!")
        break


