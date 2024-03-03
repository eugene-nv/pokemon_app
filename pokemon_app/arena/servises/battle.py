import random

from pokemon.models import Pokemon
from arena.models import Arena, Log
from pokemon.servises.level import AfterBattle


class CreateBattle:
    def __init__(self, user):
        self.pokemon_db = Pokemon
        self.arena_db = Arena
        self.user = user

    def create_battle(self, pokemons):
        return self.arena_db.objects.create(owner_pokemon=pokemons[0], enemy_pokemon=pokemons[1])

    def choose_pokemon_for_battle(self):
        owner_pokemon = random.choice(self.pokemon_db.objects.filter(owner=self.user))
        enemy_pokemon = random.choice(
            list((pokemon for pokemon in self.pokemon_db.objects.all() if pokemon.owner != self.user)))

        return [owner_pokemon, enemy_pokemon]

    def shuffle_pokemons(self, pokemons):
        random.shuffle(pokemons)
        return pokemons


class Logging:
    log_db = Log

    def log(self, battle, action, winner=None):
        self.log_db.objects.create(
            battle=battle,
            action=action,
            winner=winner,
        )


class Battle(CreateBattle, Logging, AfterBattle):
    def __init__(self, user):
        super().__init__(user)
        self.after_battle = AfterBattle()

    def is_alive(self, pokemon):
        return pokemon.hp > 0

    def damage(self, pokemon):
        return random.randint(1, pokemon.strength)

    def battle(self):
        pokemons = self.choose_pokemon_for_battle()
        result = self.create_battle(pokemons)
        self.shuffle_pokemons(pokemons)

        first = pokemons[0]
        second = pokemons[1]

        print(f'Бой {first.name} ({first.owner}) против {second.name} ({second.owner}).')
        print(f'{second.name}\nЗдоровье {second.hp}\n\n')
        print(f'{first.name}\nЗдоровье {first.hp}\n\n')

        while True:
            if self.is_alive(first):
                damage = self.damage(first)
                second.hp -= damage
                action = f'{first.name} наносит урон {damage} - у {second.name} остается {second.hp} хп'
                self.log(result, action)
                print(action)
                if self.is_alive(second):
                    damage = self.damage(second)
                    first.hp -= damage
                    action = f'{second.name} наносит урон {damage} - у {first.name} остается {first.hp} хп'
                    self.log(result, action)
                    print(action)
                else:
                    print(f'{first.name} выйграл')
                    action = f'{first.name} выйграл'
                    AfterBattle.after_battle(first, second)
                    result.result = first.name
                    result.save()
                    self.log(result, action, result.result)
                    break
            else:
                print(f'{second.name} выйграл')
                action = f'{first.name} выйграл'
                AfterBattle.after_battle(second, first)
                result.result = second.name
                result.save()
                self.log(result, action, result.result)
                break
