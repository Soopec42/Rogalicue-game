from abc import ABC, abstractclassmethod
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
    
    def player_turn(self, action_key, target_index=0):
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
        self.current_combat = None
        self.game_data = {
            'current_level': 1,
            'total_turns': 0,
            'enemies_defeated': 0
        }
    
    
    def start_new_game(self, player_name):
        self.player = Player(player_name)
        self.game_data = {'current_level': 1, 'total_turns': 0, 'enemies_defeated': 0}
        self.state = GameState.EXPLORATION
        self._generate_encounter()
    
    def process_player_input(self, input_data):
        """Обработать ввод игрока в зависимости от состояния"""
        if self.state == GameState.COMBAT:
            return self._process_combat_input(input_data)
        elif self.state == GameState.EXPLORATION:
            return self._process_exploration_input(input_data)
        elif self.state == GameState.INVENTORY:
            return self._process_inventory_input(input_data)
    
    def update_game_state(self):
        """Обновить состояние игры"""
        if self.state == GameState.COMBAT and self.current_combat:
            if self.current_combat.is_combat_over():
                result = self.current_combat.get_combat_result()
                self._handle_combat_end(result)
    
    def render_game_screen(self):
        """Отрисовать текущий экран игры"""
        if self.state == GameState.COMBAT:
            self._render_combat_screen()
        elif self.state == GameState.EXPLORATION:
            self._render_exploration_screen()
        elif self.state == GameState.MAIN_MENU:
            self._render_main_menu()
    
    # Приватные методы для различных состояний
    def _process_combat_input(self, input_data):
        """Обработка ввода в режиме боя"""
        if input_data in ['1', '2', '3', '4', '5']:
            return self.current_combat.player_turn(input_data)
        elif input_data == 'flee':
            return self._attempt_flee()
        return False
    
    def _process_exploration_input(self, input_data):
        """Обработка ввода в режиме исследования"""
        if input_data == 'explore':
            self._generate_encounter()
        elif input_data == 'inventory':
            self.state = GameState.INVENTORY
        elif input_data == 'rest':
            self._rest_player()
    
    def _generate_encounter(self):
        """Создать случайную встречу"""
        enemy_types = [
            Enemy("Гоблин", 30, 8, 3, "warrior"),
            Enemy("Орк", 50, 12, 5, "warrior"),
            Enemy("Маг", 25, 15, 2, "mage"),
            Enemy("Жрец", 35, 10, 4, "healer")
        ]
        
        num_enemies = random.randint(1, 3)
        enemies = random.choices(enemy_types, k=num_enemies)
        
        # Создаем копии врагов
        encounter = []
        for i, enemy_template in enumerate(enemies):
            new_enemy = Enemy(
                f"{enemy_template.name} {i+1}",
                enemy_template.max_health,
                enemy_template.attack_power,
                enemy_template.defense,
                enemy_template.enemy_type
            )
            encounter.append(new_enemy)
        
        self.current_combat = Combat(self.player, encounter)
        self.state = GameState.COMBAT
    
    def _handle_combat_end(self, result):
        """Обработать окончание боя"""
        if result == "victory":
            self.game_data['enemies_defeated'] += len(self.current_combat.enemies)
            self._reward_player()
            self.state = GameState.EXPLORATION
        elif result == "defeat":
            self.state = GameState.GAME_OVER
    
    def _reward_player(self):
        """Наградить игрока за победу"""
        xp_gain = 20 * self.game_data['current_level']
        self.player.experience += xp_gain
        self._check_level_up()
    
    def _check_level_up(self):
        """Проверить повышение уровня"""
        required_xp = self.player.level * 100
        if self.player.experience >= required_xp:
            self.player.level += 1
            self.player.max_health += 10
            self.player.health = self.player.max_health
            self.player.max_mana += 5
            self.player.mana = self.player.max_mana
    
    # Методы рендеринга
    def _render_combat_screen(self):
        """Отрисовать экран боя"""
        print(f"\n=== БОЙ (Ход {self.current_combat.turn_count + 1}) ===")
        print(f"Игрок: {self.player.health}/{self.player.max_health} HP | "
              f"{self.player.mana}/{self.player.max_mana} Mana")
        
        print("\nВраги:")
        for i, enemy in enumerate(self.current_combat.enemies):
            status = "💀" if not enemy.is_alive else "❤️"
            print(f"{i+1}. {enemy.name}: {enemy.health}/{enemy.max_health} HP {status}")
        
        print("\nСпособности:")
        for key, ability in self.player.abilities.items():
            status = "✅" if ability.is_ready() else f"⏳{ability.current_cooldown}"
            print(f"{key}. {ability.name} {status}")
    
    def _render_exploration_screen(self):
        """Отрисовать экран исследования"""
        print(f"\n=== ИССЛЕДОВАНИЕ ===")
        print(f"Уровень: {self.game_data['current_level']} | "
              f"Побеждено врагов: {self.game_data['enemies_defeated']}")
        print(f"Здоровье: {self.player.health}/{self.player.max_health} | "
              f"Уровень: {self.player.level}")
        print("\nДоступные действия: explore, inventory, rest")
    
    def _render_main_menu(self):
        """Отрисовать главное меню"""
        print("=== ГЛАВНОЕ МЕНЮ ===")
        print("1. Новая игра")
        print("2. Загрузить игру")
        print("3. Выход")

class Printer():
    pass
        
    

def main():
    pass



if __name__ == "__main__":
    main()  
