from pokemon.models import Pokemon
from pokemon.servises.components import Entity, Name, Portrait, Experience, Level, Strength, Constitution, Health
from .names import names


class PokemonSystem:
    pokemons_names = names

    def __init__(self):
        self.entry = Entity()

    def create_pokemon(self, user):
        self.entry.user = user
        self.entry.name = Name().random_choice_name(PokemonSystem.pokemons_names)
        self.entry.portrait = Portrait(portrait=f'portrait/{self.entry.name}.png').portrait
        self.entry.experience = Experience().experience
        self.entry.level = Level().level
        self.entry.strength = Strength(8, 12).strength
        self.entry.constitution = Constitution(8, 12).constitution
        self.entry.health = Health(self.entry.constitution, min=1, max=8).health

        pokemon = Pokemon.objects.create(
            owner=user,
            name=self.entry.name,
            portrait=self.entry.portrait,
            experience=self.entry.experience,
            level=self.entry.level,
            strength=self.entry.strength,
            constitution=self.entry.constitution,
            hp=self.entry.health,
        )
        return pokemon

    @staticmethod
    def get_pokemon(pokemon_id):
        data = Pokemon.objects.get(id=pokemon_id)
        pokemon = Entity()
        pokemon.name = data.name
        pokemon.portrait = data.portrait
        pokemon.experience = data.experience
        pokemon.level = data.level
        pokemon.strength = data.strength
        pokemon.constitution = data.constitution
        pokemon.hp = data.hp
        return pokemon
