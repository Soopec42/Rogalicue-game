from abc import ABC, abstractmethod
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

    def __init__(self, name, cooldown, damage=0, healing=0, poison = 0, burne = 0, shield = 0, splash = None):
        self._name = name
        self._cooldown = cooldown
        self._current_cooldown = 0
        self._damage = damage
        self._healing = healing
        self._poison = poison
        self._burne = burne
        self._shield = shield
        self._splash = splash


    #@abstractmethod
    #def spell(self):
    #    pass


    def is_ready(self):
        return self._current_cooldown == 0

    def use(self):
        if self._current_cooldown == 0:
            print(f"Использована способность: {self.name}")
            self._current_cooldown = self._cooldown
            return True
        else:
            print(f"Способность {self.name} перезаряжается. Осталось ходов: {self._current_cooldown}")
            return False
    
    def update(self):
        if self._current_cooldown > 0:
            self._current_cooldown -= 1


class Fireball(Ability):
    def __init__(self, name='fireball', cooldown =5, damage = 5, healing=0, poison = 0, burne = 2, shield = 0, splash = 'close'):
        super().__init__(name, cooldown, damage, healing, poison, burne, shield, splash)


class Heal(Ability):
    def __init__(self, name="heal", cooldown = 5, damage=0, healing=20, poison = 0, burne = 0, shield = 0, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, burne, shield, splash)

class Shield(Ability):
    def __init__(self, name="shield", cooldown =4, damage=0, healing=0, poison = 0, burne = 0, shield = 15, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, burne, shield, splash)


class Lightning(Ability):
    def __init__(self, name = "lightning", cooldown = 6, damage=15, healing=0, poison = 0, burne = 0, shield = 0, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, burne, shield, splash)


class Poison(Ability):
    def __init__(self, name = "poison", cooldown = 4, damage=0, healing=0, poison = 4,  burne = 0, shield = 0, splash = None):
        super().__init__(name, cooldown, damage, healing, poison, burne, shield, splash)

class AbilityCards:
    @staticmethod
    def get_cards():
       return {
            'fireball': [
                "┌───────────────┐",
                "│  ОГНЕННЫЙ ШАР │",
                "│               │",
                "│      /\\\      │",
                "│     (  )      │",
                "│    (    )     │",
                "│   /------\\\   │",
                "│  |  ОГОНЬ ||  │",
                "│   \______//   │",
                "│               │",
                "│ Урон: 5       │",
                "│ Перезаряд: 5  │",
                "└───────────────┘"
            ],
            'heal': [
                "┌───────────────┐",
                "│    ЛЕЧЕНИЕ    │",
                "│               │",
                "│      +++      │",
                "│     +   +     │",
                "│    +  Л  +    │",
                "│     +   +     │",
                "│      +++      │",
                "│       +       │",
                "│               │",
                "│ Лечение: 20   │",
                "│ Перезаряд: 5  │",
                "└───────────────┘"
            ],
            'shield': [
                "┌───────────────┐",
                "│      ЩИТ      │",
                "│               │",
                "│     /\\_/\\   │",
                "│    ( o.o )    │",
                "│     > ^ <     │",
                "│    /  |  \\   │",
                "│   /   |   \\  │",
                "│  /_________\\ │",
                "│               │",
                "│ Защита: 15    │",
                "│ Перезаряд: 4  │",
                "└───────────────┘"
            ],
            'lightning': [
                "┌───────────────┐",
                "│    МОЛНИЯ     │",
                "│               │",
                "│      /\\      │",
                "│     /  \\     │",
                "│    /    \\    │",
                "│   /  ZZ  \\   │",
                "│  /________\\  │",
                "│    /    /     │",
                "│               │",
                "│ Урон: 15(всем)│",
                "│ Перезаряд: 6  │",
                "└───────────────┘"
            ],
            'poison': [
                "┌───────────────┐",
                "│      ЯД       │",
                "│               │",
                "│     . . .     │",
                "│    .  @  .    │",
                "│   .   @   .   │",
                "│    .  @  .    │",
                "│     '   '     │",
                "│      ~ ~      │",
                "│               │",
                "│ Яд: 4/ход     │",
                "│ Длит: 4 хода  │",
                "└───────────────┘"
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

class Entiti(ABC):
    @abstractmethod
    def take_damage(self, damage):
        pass
    
    @abstractmethod
    def is_alive(self):
        pass

    def __init__(self, name, health = 100, damage = 10, abilities = [], poisoned = 0, burned = 0, shield = 0):
        self._name = name
        self._health = health
        self._damage = damage
        self._maxHealth = health
        self._abilities = abilities
        self._poisoned = poisoned
        self._burned = burned
        self._shield = shield

        @property
        def health(self):
            return self._health

   
        @health.setter
        def health(self, new_health):
            if new_health > 0 and new_health <= self._maxHealth:
                self._health = new_health
            elif new_health > self._maxHealth:
                self._health = self._maxHealth
            else:
                self._health = 0

        @property
        def damage(self):
            return self._damage

        @damage.setter
        def damage(self, new_damage):
            if new_damage > 0:
                self._health = new_damage
            else:
                self._health = 0

    def take_damage(self, damage):
        actual_damage = damage
        if self._shield > 0:
            if self._shield >= actual_damage:
                self._shield -= actual_damage
                actual_damage = 0
            else:
                actual_damage -= self._shield
                self._shield = 0
        self.health = self.health - actual_damage

    def heal(self, amount):
        self._health = min(self._maxHealth, self._health + amount)

    def is_alive(self):
        return self._health > 0

    @abstractmethod
    def update():
        pass

class Character(Entiti):
   

    def update(self):
        if self._poisoned > 0:
            self.take_damage(4)
            self._poisoned -= 1
        if self._burned > 0:
            self.take_damage(3)
            self._burned -= 1

    def end_turn(self):
        self.update()
        for ability in self._abilities:
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

class Entity(Entiti):
    

    
    def update(self):
        if self._poisoned > 0:
            self.take_damage(4)
            self._poisoned -= 1
        if self._burned > 0:
            self.take_damage(3)
            self._burned -= 1
    
    
    
    

class Combat:
    def __init__(self, player, enemies):
        self._player = player
        self._enemies = enemies
        self._turn_count = 0
        self._target = 0
        self._card = None
    
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
            print("\nВыберите действие:")
            print("   1. Выбрать цель")
            print("   2. Атаковать")
            print("   3. Использовать карту")
            while True:
                try:
                    action = int(input("Ваш выбор: "))
                    break
                except Exception:
                    print("Пожалуйста, введите число")
                
            if action == 1:
                print("\nДоступные цели:")
                for i in range(0, len(self._enemies)):
                    print(f"   {i + 1}. {self._enemies[i]._name} |  {self._enemies[i]._health}/{self._enemies[i]._maxHealth}")
                
                while True:
                    try:
                        target = int(input("Выберите цель: "))
                        if target <= len(self._enemies):
                            self._target = target - 1
                            print(f"Цель выбрана: {self._enemies[self._target]._name}")
                            break
                        else:
                            print(f"Введите число от 1 до {len(self._enemies)}")
                            continue
                    except Exception:
                        print("Пожалуйста, введите число")
                    
                    
                    
            # ['fireball', 'heal', 'shield', 'lightning', 'poison']
            elif action == 2:
                if self._card  != None:
                    ability = self._player._abilities[self._card]
                    print(f"\nИспользована способность: {ability._name}!")
                    if ability._damage > 0:
                        print(f"Нанесено доп урона: {ability._damage}")
                    if ability._healing > 0:
                        print(f"Получено лечения: {ability._healing}")
                    if ability._shield > 0:
                        print(f"Добавлено щита: {ability._shield}")
                    if ability._name in ['fireball', 'heal', 'shield', 'poison']:
                        self._enemies[self._target].take_damage(self._player.damage + ability._damage)
                    else:
                        for i in range(0, len(self._enemies)):
                            self._enemies[self._target].take_damage(ability._damage)
                    self._enemies[self._target]._poisoned += (ability._poison)
                    self._enemies[self._target]._burned += (ability._burne)
                    if self._player._abilities[self._card]._splash == 'close':
                        if len(self._enemies) > self._target + 1:
                            self._enemies[self._target + 1]._burned += (ability._burne)
                            self._enemies[self._target + 1]._poisoned += (ability._poison)
                        if (self._target - 1) != -1:
                            self._enemies[self._target - 1]._burned += (ability._burne)
                            self._enemies[self._target - 1]._poisoned += (ability._poison)
                    self._player._shield += ability._shield
                    self._player.heal(ability._healing)
                    ability._current_cooldown = ability._cooldown
                else:
                    self._enemies[self._target].take_damage(self._player.damage)
                self._card = None
                self._player.end_turn()
                for id in range(len(self._enemies) - 1, -1, -1):
                    if self._enemies[id].health <= 0:
                        print(f"{self._enemies[id]._name} defeated!")
                        self._enemies.pop(id)
                        self._target = 0
                break
                

            elif action == 3:
                print("\nВАШИ КАРТЫ:")
                AbilityCards.display_ability_hand(self._player._abilities)
                print("\nПерезарядка:")
                for i in range(0, len(self._player._abilities)):
                    cd_status = "Готово" if self._player._abilities[i]._current_cooldown == 0 else f" {self._player._abilities[i]._current_cooldown} ход(ов)"
                    print(f"   {i+1}. {cd_status}")
                if len(self._player._abilities) > 0:
                    while True:
                        try:
                            num_card = int(input("Выберите номер карты: "))
                            if num_card <= len(self._player._abilities):
                                if self._player._abilities[num_card - 1].is_ready():
                                    self._card = num_card - 1
                                    print(f"Карта '{self._player._abilities[self._card]._name}' выбрана!")
                                    break   
                                else:
                                    print(f"Карта на перезарядке! Осталось: {self._player._abilities[num_card - 1]._current_cooldown} ход(ов)")
                                    break
                            else:
                                print(f"Введите число от 1 до {len(self._player._abilities)}")
                            
                        except Exception:
                            print("Пожалуйста, введите число")
                    
                            
                    
                    
            else:
                print("not correct")
                continue



    def show_state(self):
        print(f"Player: {self._player._name} | HP: {self._player.health}/{self._player._maxHealth} | Shield: {getattr(self._player, '_shield', 0)}")
        print("Enemies:")
        for i, enemy in enumerate(self._enemies):
            status_effects = []
            if getattr(enemy, '_poisoned', 0) > 0:
                status_effects.append(f"Poisoned({enemy._poisoned})")
            if getattr(enemy, '_burned', 0) > 0:
                status_effects.append(f"Burned({enemy._burned})")
            if getattr(enemy, '_shield', 0) > 0:
                status_effects.append(f"Shield({enemy._shield})")
        
            status_str = " | " + ", ".join(status_effects) if status_effects else ""
            print(f"  {i+1}. {enemy._name} | HP: {enemy.health}/{enemy._maxHealth}{status_str}")


    def enemy_turn(self):
        for enemy in self._enemies:
            self._player.take_damage(enemy.damage)
            enemy.update()
        
        
        
    
    def is_combat_over(self):
        player_alive = self._player.is_alive()
        enemies_alive = len(self._enemies) > 0
    
        if not player_alive:
            return True
        elif not enemies_alive:
            return True
        return False
    
    def get_combat_result(self):
        if not self._player.is_alive():
            print("\nПОРАЖЕНИЕ! Ваш персонаж пал в бою...")
        elif len(self._enemies) == 0:
            print("\nПОБЕДА! Все противники повержены!")

class Game():


    def start_fight(self, fight):
        while not fight.is_combat_over():
            fight.player_turn()
            if fight.is_combat_over():
                fight.get_combat_result()
                break
            fight.enemy_turn()
            if fight.is_combat_over():
                fight.get_combat_result()
                break
            fight.show_state()
           
       
    
    def create_enemy(self, char_type, name):
        enemy = self.factory.create_character(char_type, name)
        self.enemies.append(enemy)
        return enemy  
    



    

def main():
    
    fireball1 = CardFactory.create_card('fireball')
    fireball2 = CardFactory.create_card('fireball')
    heal1 = CardFactory.create_card('heal')
    troll = Entity("troll", 50, 10)
    knight =  Entity("knight", 50, 10)
    enemies = [troll, knight]
    player = Warrior("warrior1", 100, 15, abilities = [fireball1, fireball2, heal1])
    fight = Combat(player, enemies)
    st = Game()
    st.start_fight(fight)


if __name__ == "__main__":
    main()  
