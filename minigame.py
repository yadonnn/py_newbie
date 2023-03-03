import random

class Player:
    def __init__(self, hp, atk, defense):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.defend = False

    def attack(self, monster):
        if not monster.defend:
            monster.hp = max(0, monster.hp - self.atk)
            print("Player dealt", self.atk, "damage to the monster!")
        else:
            print("The monster blocked the player's attack!")

    def defend(self):
        self.defend = True
        print("The player is defending!")

    def hit(self, damage):
        if self.defend:
            print("The player blocked the monster's attack!")
            self.defend = False
        else:
            self.hp = max(0, self.hp - damage)
            print("The monster dealt", damage, "damage to the player!")
            if self.hp == 0:
                print("The player is defeated!")

class Monster:
    def __init__(self, hp, atk, defense):
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.defend = False

    def attack(self, player):
        if not player.defend(player):
            damage = max(0, self.atk - player.defense)
            player.hit(damage)
        else:
            print("The player blocked the monster's attack!")
    
    def defend(self):
        self.defend = True
        print("The monster is defending!")

    def hit(self, damage):
        if self.defend:
            print("The monster blocked the player's attack!")
            self.defend = False
        else:
            self.hp = max(0, self.hp - damage)
            print("Player dealt", damage, "damage to the monster!")
            if self.hp == 0:
                print("The monster is defeated!")


player = Player(100, 10, 5)
monster = Monster(80, 8, 3)

while player.hp > 0 and monster.hp > 0:
    print("Player HP:", player.hp)
    print("Monster HP:", monster.hp)
    action = input("Enter a for attack, d for defend: ")
    if action == 'a':
        player.attack(monster)
    elif action == 'd':
        player.defend
    else:
        print("Invalid input! Try again.")
        continue

    if random.randint(0, 1) == 0:
        monster.attack(player)
    else:
        monster.defend

print("Game over!")