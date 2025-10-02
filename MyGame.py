from abc import ABC, abstractclassmethod
from enum import Enum
import random

from networkx import is_attracting_component

class GameState(Enum):
    MAIN_MENU = "main_menu"
    COMBAT = "combat"
    EXPLORATION = "exploration"
    INVENTORY = "inventory"
    CHARACTER = "character"
    GAME_OVER = "game_over"
    VICTORY = "victory"

class EntityType(Enum):
    PLAYER = "player"
    ENEMY = "enemy"
    NPC = "npc"

class Ability:

    def __init__(self, name, cooldown, damage=0, healing=0, poison = 0):
        self._name = name
        self._cooldown = cooldown
        self._current_cooldown = 0
        self._damage = damage
        self._healing = healing
        self._poison = poison

    @abstractclassmethod
    def spell(self):
        pass


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


class Character:
    def __init__(self, name, health, damage, abilities = {}):
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
    def __init__(self, name, health, damage):
        super().__init__(name. health, damage)
    
class Magician(Character):
    def __init__(self, name, health, damage):
        super().__init__(name. health, damage)   

class Assasin(Character):
    def __init__(self, name, health, damage):
        super().__init__(name. health, damage)

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
        self.current_turn = "player"
    
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
            action = input()
            if action == 1:
                



            for enemy in self._enemies:



        target = self.enemies[target_index] if self.enemies else None
        success, result = self.player.use_ability(action_key, target)

        self.enemies = [enemy for enemy in self.enemies if enemy.is_alive]
        
        self.current_turn = "enemy"
        return success
    
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
    pass



if __name__ == "__main__":
    main()  
