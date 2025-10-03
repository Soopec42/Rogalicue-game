from abc import ABC, abstractclassmethod
import string
from enum import Enum
import random

class GameState(Enum):
    MAIN_MENU = "main_menu"
    COMBAT = "combat"
    EXPLORATION = "exploration"
    INVENTORY = "inventory"
    CHARACTER = "character"
    GAME_OVER = "game_over"
    VICTORY = "victory"


    


class CardFactory:
    @staticmethod
    def create_card(card_type):
        if card_type == "fireball":
            return Fireball()
        elif card_type == "heal":
            return Heal()
        elif card_type == "shield":
            return Shield()
        elif card_type == "lightning":
            return Lightning()
        elif card_type == "poison":
            return Poison()


class Ability:

    def __init__(self, name, cooldown, damage=0, healing=0, poison = 0, poison_dmg = 0, shield = 0, splash = None):
        self._name = name
        self._cooldown = cooldown
        self._current_cooldown = 0
        self._damage = damage
        self._healing = healing
        self._poison = poison
        self._poison_dmg = poison_dmg


    #@abstractclassmethod
    #def spell(self):
    #    pass


    def is_ready(self):
        return self._current_cooldown == 0

    def use(self):
        if self.current_cooldown == 0:
            print(f"Использована способность: {self.name}")
            self.current_cooldown = self.cooldown
            return True
        else:
            print(f"Способность {self.name} перезаряжается. Осталось ходов: {self.current_cooldown}")
            return False
    
    def update(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1


class Fireball(Ability):
    def __init__(self, name='fireball', cooldown =5, damage = 22, healing=0, poison = 2, poison_dmg = 3, shield = 0, splash = 'close'):
        super().__init__(name, cooldown, damage, healing, poison, poison_dmg, shield, splash)


class Heal(Ability):
    def __init__(self, name="heal", cooldown = 5, damage=0, healing=30, poison = 0, poison_dmg = 0, shield = 0, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, poison_dmg, shield, splash)

class Shield(Ability):
    def __init__(self, name="shield", cooldown =4, damage=0, healing=0, poison = 0, poison_dmg = 0, shield = 15, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, poison_dmg, shield, splash)


class Lightning(Ability):
    def __init__(self, name = "lightning", cooldown = 6, damage=25, healing=0, poison = 0, poison_dmg = 0, shield = 0, splash = "full"):
        super().__init__(name, cooldown, damage, healing, poison, poison_dmg, shield, splash)


class Poison(Ability):
    def __init__(self, name = "poison", cooldown = 4, damage=0, healing=0, poison = 0, poison_dmg = 0, shield = 0, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, poison_dmg, shield, splash)

class AbilityCards:
    @staticmethod
    def get_cards():
        return {
            'fireball': [
                "┌───────────────┐",
                "│   FIREBALL    │",
                "│               │",
                "│      /\\\      │",
                "│     (  )      │",
                "│    (    )     │",
                "│   /------\\\   │",
                "│  |  FIRE  ||  │",
                "│   \______//   │",
                "│               │",
                "│ Damage: 25    │",
                "│ Cooldown: 5   │",
                "└───────────────┘"
            ],
            'frost': [
                "┌───────────────┐",
                "│    FROST      │",
                "│               │",
                "│     * * *     │",
                "│    *  *  *    │",
                "│   *   *   *   │",
                "│    *  *  *    │",
                "│     * * *     │",
                "│       *       │",
                "│               │",
                "│ Freeze: 1     │",
                "│ Cooldown: 6   │",
                "└───────────────┘"
            ],
            'heal': [
                "┌───────────────┐",
                "│      HEAL     │",
                "│               │",
                "│      +++      │",
                "│     +   +     │",
                "│    +  H  +    │",
                "│     +   +     │",
                "│      +++      │",
                "│       +       │",
                "│               │",
                "│ Heal: 30 HP   │",
                "│ Cooldown: 5   │",
                "└───────────────┘"
            ],
            'shield': [
                "┌───────────────┐",
                "│     SHIELD    │",
                "│               │",
                "│    _______    │",
                "│   /       \\  │",
                "│  |  SHIELD || │",
                "│   \       //  │",
                "│    \     //   │",
                "│     \___//    │",
                "│               │",
                "│ Block: 15 dmg │",
                "│ Cooldown: 4   │",
                "└───────────────┘"
            ],
            'lightning': [
                "┌────────────────┐",
                "│   LIGHTNING    │",
                "│                │",
                "│      /\\       │",
                "│     /  \\      │",
                "│    /    \\     │",
                "│   /  ZZ  \\    │",
                "│  /________\\   │",
                "│    /    /      │",
                "│                │",
                "│ Damage: 25     │",
                "│ Cooldown: 6    │",
                "└────────────────┘"
            ],
            'poison': [
                
                "┌────────────────┐",
                "│    POISON      │",
                "│                │",
                "│     . . .      │",
                "│    .  @  .     │",
                "│   .   @   .    │",
                "│    .  @  .     │",
                "│     '   '      │",
                "│      ~ ~       │",
                "│                │",
                "│ Damage: 5/3 tur│",
                "│ Duration: 4    │",
                "└────────────────┘"


            ],
            'berserk': [
                "┌────────────────┐",
                "│   BERSERK      │",
                "│                │",
                "│     /\\_/\\    │",
                "│    ( o.o )     │",
                "│     > ^ <      │",
                "│    /  |  \\    │",
                "│   /   |   \\   │",
                "│  /_________\\  │",
                "│                │",
                "│ +10 DMG 3 T    │",
                "│ COOLDOWN: 7    │",
                "└────────────────┘"
            ]
            
        }
    
    @staticmethod
    def display_card(card_name):
        cards = AbilityCards.get_cards()
        if card_name in cards:
            for line in cards[card_name]:
                print(line)
        else:
            print(f"Card '{card_name}' not found")
    
    @staticmethod   
    def display_hand(card_names):
        cards = AbilityCards.get_cards()
        hand = [cards[name] for name in card_names if name in cards]
        
        if not hand:
            print("No valid cards in hand")
            return
        
        for line_num in range(len(hand[0])):
            for card in hand:
                print(card[line_num], end="  ")
            print()

    @staticmethod
    def display_ability_hand(ability_objects):
        card_names = []
        for ability in ability_objects:
            card_names.append(ability._name)
        
        AbilityCards.display_hand(card_names)

    @staticmethod
    def display_hand(card_names):
        cards = AbilityCards.get_cards()
        hand = [cards[name] for name in card_names if name in cards]
        
        if not hand:
            print("No valid cards in hand")
            return
        
        for line_num in range(len(hand[0])):
            for card in hand:
                print(card[line_num], end="  ")
            print()

class Character:
    def __init__(self, name, health, damage, abilities = []):
        self._name = name
        self._health = health
        self._damage = damage
        self._maxHealth = health
        self._abilities = abilities


    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_heath):
        if not new_heath.isdight():
            print("ошибка хп")
        elif new_heath > 0:
            self._health = new_heath
        else:
            self._health = 0

    @property
    def damage(self):
        return self._health

    @health.setter
    def damage(self, new_heath):
        if not new_heath.isdight():
            print("ошибка damage")
        elif new_heath > 0:
            self._health = new_heath
        else:
            self._health = 0

    def take_damage(self, damage):
        self._health = self._health - damage
        return self.health > 0

    def is_alive(self):
        return self._health > 0
    
    def heal(self, amount):
        self.health = min(self.max_health, self._health + amount)

    def end_turn(self):
        for ability in self.abilities.values():
            ability.update()


class Warrior(Character):
    def __init__(self, name, health, damage, abilities = []):
        super().__init__(name, health, damage, abilities)
    
class Magician(Character):
    def __init__(self, name, health, damage, abilities = []):
        super().__init__(name, health, damage, abilities)   

class Assasin(Character):
    def __init__(self, name, health, damage, abilities = []):
        super().__init__(name, health, damage, abilities)

class Entity():
    def __init__(self, name, health=100, max_health=100, attack=10, defense=5):
        self._name = name
        self._health = health
        self._max_health = max_health
        self._attack_power = attack
        self._defense = defense
    
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_heath):
        if not new_heath.isdight():
            print("ошибка хп")
        elif new_heath > 0:
            self._health = new_heath
        else:
            self._health = 0

    @property
    def damage(self):
        return self._health

    @health.setter
    def damage(self, new_heath):
        if not new_heath.isdight():
            print("ошибка damage")
        elif new_heath > 0:
            self._health = new_heath
        else:
            self._health = 0

    def take_damage(self, damage):
        self._health = self._health - damage
        

    def is_alive(self):
        return self._health > 0
    
    def heal(self, amount):
        self._health = min(self._max_health, self._health + amount)
    
    

class Combat:
    def __init__(self, player, enemies):
        self._player = player
        self._enemies = enemies
        self._turn_count = 0
        self._target = 0
        self._card = None
        self.current_turn = "player"
        self._mass = False
    
    def choose_your_target(enemies):
        target = input("Who is your target? ")
        inc = True
        while inc:
            if target > len(enemies):
                print("Num out of range! ")
                continue
            else:
                return target
    
    def player_turn(self):
        move = True
        while move:
            print("Choose your action: ")
            print("1. Choose target")
            print("2. Attack")
            print("3. Use a card")
            while True:
                try:
                    action = int(input())
                    break
                except Exception:
                    print("Пожалуйста, введите целое число")
                
            if action == 1:
                
                for i in range(0, len(self._enemies)):
                    print(f"{(i + 1)} {self._enemies[i]._name}")
                
                while True:
                    try:
                        target = int(input("Choose the target: "))
                        if target <= len(self._enemies):
                            self._target = target - 1
                            break
                        else:
                            print("Пожалуйста, введите корректный номер карты")
                            continue
                    except Exception:
                        print("Пожалуйста, введите целое число")
                    
                    
                    

            elif action == 2:
                if self._card == None:
                    pass
                else:
                    pass
                #target = 0
                #сводим все выбраные параметры к базовым
                #проверка что мы не нахилим сверх нормы

            elif action == 3:
                AbilityCards.display_ability_hand(self._player._abilities)
                for i in range(0, len(self._player._abilities)):
                    print(f"Current cd: {self._player._abilities[i]._current_cooldown}", end = "      ")
                if len(self._player._abilities) > 0:
                    while True:
                        try:
                            num_card = int(input("Choose the card number: "))
                            if num_card <= len(self._player._abilities):
                                if self._player._abilities[num_card - 1].is_ready():
                                    self._card = num_card - 1
                                    break   
                                else:
                                    print(f"card in cooldown {self._player._abilities[num_card - 1].cooldown} more second")
                                    break
                            else:
                                print("Пожалуйста, введите корректное число")
                            
                        except TypeError:
                            print("Пожалуйста, введите целое число")
                    
                            
                    
                    
            else:
                print("not correct")
                continue



            


    def enemy_turn(self):
        for enemy in self.enemies:
            if enemy.is_alive:
                result = enemy.take_turn(self.player)
        
        self.current_turn = "player"
        self.turn_count += 1
        self.player.end_turn()
    
    def is_combat_over(self):
        return not self.player.is_alive or len(self.enemies) == 0
    
    def get_combat_result(self):
        if not self.player.is_alive:
            return "defeat"
        elif len(self.enemies) == 0:
            return "victory"
        return "ongoing"

class Game():

    def __init__(self):
        self.state = GameState.MAIN_MENU
        self.player = None
        self.enemies = []

    def start_fight(self, player, enemies):
        fight = Combat(player, enemies)
        going = True
        while going:
            fight.player_turn()
            fight.enemies_turn()
            if fight.is_attracting_component():
                fight.get_combat_result()
                break
           
       
    
    def create_enemy(self, char_type, name):
        enemy = self.factory.create_character(char_type, name)
        self.enemies.append(enemy)
        return enemy  
    




    
    

class Printer():
    pass
        
    

def main():
    
    fireball1 = CardFactory.create_card('fireball')
    fireball2 = CardFactory.create_card('fireball')
    heal1 = Heal()
    troll = Entity("troll", 50, 50, 10, 0)
    knight =  Entity("knight", 50, 50, 10, 5)
    enemies = [troll, knight]
    player = Warrior("warrior1", 100, 15, abilities = [fireball1, fireball2])
    fight = Combat(player, enemies)
    fight.player_turn()



if __name__ == "__main__":
    main()  
