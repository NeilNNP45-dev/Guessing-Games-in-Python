import random
class Character:
    def __init__(self, name, health, normal_min=5, normal_max=10, strong_min=15, strong_max=25):
        self.name = name
        self.health = health
        self.used_strong_last_turn = False
        self.normal_min = normal_min
        self.normal_max = normal_max
        self.strong_min = strong_min
        self.strong_max = strong_max

    def normal_attack(self, target):
        damage = random.randint(self.normal_min, self.normal_max)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")        

    def strong_attack(self, target):
        if self.used_strong_last_turn:
            print(f"{self.name} cannot use strong attack this turn!")
            return False
        damage = random.randint(self.strong_min, self.strong_max)
        target.health -= damage
        self.used_strong_last_turn = True
        print(f"{self.name} uses a strong attack on {target.name} for {damage} damage!")
        return True
        
class Knight(Character):
     def __init__(self, name):
        super().__init__(name, 120, normal_min=5, normal_max=10, strong_min=15, strong_max=25)
class Mage(Character):
    def __init__(self, name):     
        super().__init__(name, 80, normal_min=8, normal_max=15, strong_min=20, strong_max=35)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 100, normal_min=7, normal_max=12, strong_min=18, strong_max=28)
  
    

def battle(player, enemy):
        while player.health > 0 :
            print(f"\n{player.name}'s Health: {player.health} | {enemy.name}'s Health: {enemy.health}")
            action = input("Choose your action (1: Normal Attack, 2: Strong Attack): ")
            if action == '1':
                player.normal_attack(enemy)
                player.used_strong_last_turn = False
            elif action == '2':
                if  player.used_strong_last_turn == True:
                    print(f"{player.name} cannot use strong attack this turn!")
                    continue
                elif player.strong_attack(enemy):
                    player.used_strong_last_turn = True
                    
            else:
                print("Invalid action. Please choose again.")
                continue            

            if enemy.health <= 0:
                print(f"{enemy.name} has been defeated! You win!")
                break

            enemy_action = random.choice(['normal', 'strong'])
            if enemy_action == 'strong' and not enemy.used_strong_last_turn == True:
                enemy.strong_attack(player)

            else:
                enemy.normal_attack(player)
                enemy.used_strong_last_turn = False

        if player.health <= 0:
          print(f"{player.name} has been defeated! Game Over!")

environments = {
    "Forest": {"Goblin": 80, "Orc": 100, "Skeleton": 60},
    "Dungeon": {"Goblin": 60, "Orc": 120, "Skeleton": 80},
    "Cave": {"Goblin": 70, "Orc": 90, "Skeleton": 100}
}
env = random.choice(list(environments.keys()))
print(f"You find yourself in a {env}.")
player_name = input("Enter your character's name: ")
classes = input("Choose your class (1: Knight, 2: Mage, 3: Archer): ")
if classes == '1':
    player = Knight(player_name)
elif classes == '2':
    player = Mage(player_name)
elif classes == '3':
    player = Archer(player_name)
enemy_name = random.choice(list(environments[env].keys()))
enemy = Character(enemy_name, environments[env][enemy_name])
print(f"\nA wild {enemy.name} appears!")
battle(player, enemy)
