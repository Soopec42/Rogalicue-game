from abc import abstractclassmethod
import random



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
        self.health = self.health - damage
        return self.health > 0

    def is_alive(self):
        return self.health > 0

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


class Game():

    def __init__(self, player):
        self._player = player
        self._combat = None

    def start_new_game(self):
         pass
        


    def fight(self):

        self._player.end_turn()


        
    

def main():
    pass



if __name__ == "__main__":
    main()  
