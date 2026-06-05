import random
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.used_strong_last_turn = False

    

    def normal_attack(self, target):
        damage = random.randint(5, 10)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")        

    def strong_attack(self, target):
        if self.used_strong_last_turn:
            print(f"{self.name} cannot use strong attack this turn!")
            return False
        damage = random.randint(15, 25)
        target.health -= damage
        self.used_strong_last_turn = True
        print(f"{self.name} uses a strong attack on {target.name} for {damage} damage!")
        return True
    
    

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
enemies = random.choice(list(environments[env].keys()))
print(f"You find yourself in a {env}.")
player_name = input("Enter your character's name: ")
player = Character(player_name, 100)
enemy_name = random.choice(list(environments[env].keys()))
enemy = Character(enemy_name, environments[env][enemy_name])
print(f"\nA wild {enemy.name} appears!")
Character.battle(player, enemy)
