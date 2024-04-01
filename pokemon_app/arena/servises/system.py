import random

from arena.models import Log, Arena
from pokemon.models import Pokemon
from pokemon.servises.components import Health, Strength, Experience, Level
from pokemon.servises.system import PokemonSystem
from users.models import User


class Logging:
    @classmethod
    def log(cls, battle, action):
        log = Log.objects.create(
            battle=battle,
            action=action,
        )
        return log


class ArenaSystem:
    def __init__(self):
        self.first_user = None
        self.second_user = None
        self.first_creature = None
        self.second_creature = None
        self.battle = None

    def get_users_for_battle(self, user_db):
        users = user_db.objects.all()
        users_list = []
        for user in users:
            users_list.append(user.id)
        random.shuffle(users_list)
        self.first_user = users_list[0]
        self.second_user = users_list[1]

        return self.first_user, self.second_user

    def get_creature_for_battle(self, creature_db):
        first_creature = random.choice(creature_db.objects.filter(owner=self.first_user))
        second_creature = random.choice(creature_db.objects.filter(owner=self.second_user))

        self.first_creature = PokemonSystem().get_pokemon(first_creature.id)
        self.second_creature = PokemonSystem().get_pokemon(second_creature.id)

        return first_creature, second_creature

    def create_battle(self, creatures, arena_db):
        self.battle = arena_db.objects.create(
            first_pokemon=creatures[0],
            second_pokemon=creatures[1])

    def set_battle_result(self, result):
        self.battle.result = result
        self.battle.save()

    def fight(self):
        while True:
            if Health().is_alive(self.first_creature):
                damage = Strength.damage(self.first_creature)
                Health().apply_damage(self.second_creature, damage)
                Logging.log(self.battle,
                            f'{self.first_creature.name} наносит урон {damage} - у {self.second_creature.name} '
                            f'остается {self.second_creature.hp} очков здоровья')

                if Health().is_alive(self.second_creature):
                    damage = Strength.damage(self.second_creature)
                    Health().apply_damage(self.first_creature, damage)
                    Logging.log(self.battle,
                                f'{self.second_creature.name} наносит урон {damage} - у {self.first_creature.name} '
                                f'остается {self.first_creature.hp} очков здоровья')

                else:
                    Logging.log(self.battle, f'{self.first_creature.name} выйграл')
                    self.set_battle_result(self.first_creature.name)
                    Experience.add_experience(self.battle.first_pokemon, 120)
                    if Level.check_level(self.battle.first_pokemon):
                        Level.add_level(self.battle.first_pokemon)
                    break

            else:
                Logging.log(self.battle, f'{self.second_creature.name} выйграл')
                self.set_battle_result(self.second_creature.name)
                Experience.add_experience(self.battle.second_pokemon, 120)
                if Level.check_level(self.battle.second_pokemon):
                    Level.add_level(self.battle.second_pokemon)
                break

    @staticmethod
    def start():
        x = ArenaSystem()
        x.get_users_for_battle(User)
        creatures = x.get_creature_for_battle(Pokemon)
        x.create_battle(creatures, Arena)
        x.fight()
