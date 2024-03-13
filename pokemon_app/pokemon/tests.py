from django.contrib.auth import get_user_model
from django.test import TestCase

from pokemon.models import Pokemon
from pokemon.servises.servises import CreatePokemon, pokemon_list, LevelUp

User = get_user_model()


class PokemonViewTestCase(TestCase):
    def setUp(self):
        self.user_eugene = User.objects.create(username='eugene')
        self.user_john = User.objects.create(username='john')

    def test_create_pokemon(self):
        pokemon = CreatePokemon(self.user_eugene)

        self.assertIn(pokemon.name, pokemon_list)
        self.assertEquals(pokemon.portrait, f'portrait/{pokemon.name.lower()}.jpeg')
        self.assertEquals(pokemon.experience, 0)
        self.assertEquals(pokemon.level, 1)
        self.assertIn(pokemon.strength, range(8, 13))
        self.assertIn(pokemon.constitution, range(8, 13))
        self.assertIn(pokemon.hp, range(9, 19))


class LevelUpViewTestCase(TestCase):
    def setUp(self):
        self.user_eugene = User.objects.create(username='eugene')
        self.pikachu = Pokemon.objects.create(
            owner=self.user_eugene,
            name='Pikachu',
            portrait='portrait/pikachu.jpeg',
            experience=0,
            level=1,
            strength=10,
            constitution=10,
            hp=15,
        )
        self.bulbasaur = Pokemon.objects.create(
            owner=self.user_eugene,
            name='Bulbasaur',
            portrait='portrait/bulbasaur.jpeg',
            experience=950,
            level=1,
            strength=10,
            constitution=10,
            hp=15,
        )

    def test_level_up(self):
        level_up_pikachu = LevelUp()

        level_up_pikachu.add_experience(self.pikachu)

        self.assertEquals(self.pikachu.level, 1)
        self.assertEquals(self.pikachu.experience, 100)
        self.assertEquals(self.pikachu.strength, 10)
        self.assertEquals(self.pikachu.constitution, 10)
        self.assertEquals(self.pikachu.hp, 15)

        level_up = LevelUp()
        level_up.add_experience(self.bulbasaur)

        self.assertEquals(self.bulbasaur.level, 2)
        self.assertEquals(self.bulbasaur.experience, 1050)
