import random

from pokemon.models import Pokemon

pokemon_list = ('Пикачу', 'Бульбазавр', 'Чармандер', 'Сквиртл')


class CreatePokemon:
    def __init__(self, user):
        self.user = user
        self.name = random.choice(pokemon_list)
        self.constitution = random.randint(8, 12)
        self.experience = 0
        self.level = 1
        self.strength = random.randint(8, 12)

    def create(self):
        pokemon = Pokemon.objects.create(
            owner=self.user,
            name=self.name,
            portrait=f'portrait/{self.name.lower()}.jpeg',
            experience=self.experience,
            level=self.level,
            strength=random.randint(8, 12),
            constitution=self.constitution,
            hp=self.constitution + random.randint(1, 6),
        )
        return pokemon


class LevelUp:

    @staticmethod
    def add_experience(pokemon):
        if pokemon.experience - (pokemon.level * 1000) >= 1000:
            pokemon.level += 1
            pokemon.experience += 100
            characteristic = random.choice([pokemon.strength, pokemon.constitution])
            characteristic += 1
        else:
            pokemon.experience += 100
