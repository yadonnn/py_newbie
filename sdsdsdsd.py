import random

class Player:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = False
        
    def attack_enemy(self, enemy):
        enemy.receive_damage(self.attack)
        
    def defend(self):
        self.defending = True
        
    def receive_damage(self, damage):
        if self.defending:
            print("Player defended the attack!")
            self.defending = False
        else:
            self.health = max(0, self.health - damage)
            print(f"Player took {damage} damage!")
            if self.health <= 0:
                print("Player has been defeated!")
    
class Monster:
    def __init__(self, health, attack, defense):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.defending = False
        
    def attack_player(self, player):
        player.receive_damage(self.attack - player.defense)
        
    def defend(self):
        self.defending = True
        
    def receive_damage(self, damage):
        if self.defending:
            print("Monster defended the attack!")
            self.defending = False
        else:
            self.health = max(0, self.health - damage)
            print(f"Monster took {damage} damage!")
            if self.health <= 0:
                print("Monster has been defeated!")
            
player = Player(100, 5, 0)
monster = Monster(50, 5, 0)

while player.health > 0 and monster.health > 0:
    command = input("Enter command (a = attack, d = defend): ")
    if command == "a":
        player.attack_enemy(monster)
        if monster.health > 0:
            if random.randint(0, 1) == 1:
                monster.defend()
                print("Monster is defending!")
            else:
                monster.attack_player(player)
    elif command == "d":
        player.defend()
        if random.randint(0, 1) == 1:
            monster.defend()
            print("Monster is defending!")
        else:
            monster.attack_player(player)
    else:
        print("Invalid command!")
        
    print(f"Player health: {player.health}")
    print(f"Monster health: {monster.health}")
    
print("Game over!")
