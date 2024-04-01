# import random
#
# from pokemon.models import Pokemon
# from .names import names
#
#
# class CreatePokemon:
#     def __init__(self, user):
#         self.user = user
#         self.name = random.choice(names)
#         self.portrait = f'portrait/{self.name}.png'
#         self.experience = 0
#         self.level = 1
#         self.strength = random.randint(8, 12)
#         self.constitution = random.randint(8, 12)
#         self.hp = self.constitution + random.randint(1, 6)
#
#     def create(self):
#         pokemon = Pokemon.objects.create(
#             owner=self.user,
#             name=self.name,
#             portrait=self.portrait,
#             experience=self.experience,
#             level=self.level,
#             strength=self.strength,
#             constitution=self.constitution,
#             hp=self.hp,
#         )
#         return pokemon
#
#
# class LevelUp:
#     @staticmethod
#     def add_experience(pokemon):
#         if pokemon.experience - (pokemon.level * 1000) + 100 >= 0:
#             pokemon.level += 1
#             pokemon.experience += 100
#             characteristic = random.choice(['strength', 'constitution'])
#
#             def add_characteristic():
#                 if characteristic == 'strength':
#                     pokemon.strength += 1
#                 elif characteristic == 'constitution':
#                     pokemon.constitution += 1
#                     pokemon.hp += 1
#
#             add_characteristic()
#
#         else:
#             pokemon.experience += 100
