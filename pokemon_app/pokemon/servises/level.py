import random

class LevelUp:

    @classmethod
    def is_level_up(cls, pokemon):
        return pokemon.experience - (pokemon.level * 1000) >= 1000

    @classmethod
    def add_level(cls, pokemon):
        pokemon.level += 1

    @classmethod
    def add_characteristic(cls, pokemon):
        characteristic = random.choice([pokemon.strength, pokemon.constitution])
        characteristic += 1

    @classmethod
    def level_up(cls, pokemon):
        if cls.is_level_up(pokemon):
            cls.add_level(pokemon)
            cls.add_characteristic(pokemon)


class AfterBattle(LevelUp):
    @classmethod
    def add_experience(cls, pokemon):
        pokemon.experience += 100

    @classmethod
    def add_win_count(cls, pokemon):
        pokemon.win_count += 1

    @classmethod
    def add_defeat_count(cls, pokemon):
        pokemon.defeat_count += 1

    @classmethod
    def after_battle(cls, winner, defeated):
        cls.add_experience(winner)
        cls.add_win_count(winner)
        cls.add_defeat_count(defeated)
        cls.level_up(winner)
        winner.save()
        defeated.save()
