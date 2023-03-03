import random

class Player:
    def __init__(self, hp, atk):
        self.hp = hp
        self.atk = atk
        self.shieldup = False
    
    def defend(self):
        self.shieldup = True

    def attack_enemy(self, enemy):
        enemy.receieve_damage(self.atk - enemy.armor)

    def receieve_damage(self, damage):
        if self.shieldup :
            print("플레이어가 공격을 막아냈습니다.")
            self.defending = False
        else :
            self.hp = max(0, self.hp - damage)
            print(f"플레이어가 {damage}의 데미지를 받았다.")
            if self.hp == 0:
                print("*"*15)
                print("몬스터 승리")
                print("*"*15)
        

class Monster :
    def __init__(self, hp, atk, armor):
        self.hp = hp
        self.atk = atk
        self.armor = armor
        self.shieldup = False

    def defend(self):
        self.shieldup = True    

    def attack_player(self, player):
        player.receieve_damage(self.atk)
    
    def receieve_damage(self, damage):
        if self.shieldup :
            print("몬스터가 공격을 막아냈습니다.")
            self.shieldup = False
        else :
            self.hp = max(0, self.hp - damage)
            print(f"몬스터가 {damage}의 데미지를 받았다.")
            if self.hp == 0:
                print("플레이어 WINNER")


player = Player(10, 5)
monster = Monster(10, 5, 1)

while player.hp > 0 and monster.hp > 0 :
    cmd = input("공격은 a, 방어는 d")
    if cmd == "a" :
        player.attack_enemy(monster)
        if monster.hp > 0 :
            if random.randint(0, 1) == 1:
                monster.defend()
                print("몬스터가 방어를 시작함")
            else :
                monster.attack_player(player)
    elif cmd == "d" :
        player.defend()
        if random.randint(0, 1) == 1:
            monster.defend()
            print("몬스터가 방어를 시작함")
        else :
            monster.attack_player(player)
    else :
        print("커맨드 키를 확인하시오")

    print(f"플레이어 HP : {player.hp}")
    print(f"몬스터 HP : {monster.hp}")

print("GAME OVER")