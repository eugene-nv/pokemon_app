# import random
#
# from pokemon.models import Pokemon
# from arena.models import Arena, Log
# from pokemon.servises.servises import LevelUp
# from users.models import User
#
#
# class Logging:
#     @classmethod
#     def log(cls, battle, action):
#         log = Log.objects.create(
#             battle=battle,
#             action=action,
#         )
#         return log
#
#
# class BeforeBattle:
#     def __init__(self):
#         self.battle = None
#         self.first_user = None
#         self.second_user = None
#
#     def get_users(self):
#         users = User.objects.all()
#         user_list = []
#         for user in users:
#             user_list.append(user.id)
#         random.shuffle(user_list)
#
#         self.first_user = user_list[0]
#         self.second_user = user_list[1]
#
#     def create_battle(self):
#         first_pokemon = random.choice(Pokemon.objects.filter(owner=self.first_user))
#         second_pokemon = random.choice(Pokemon.objects.filter(owner=self.second_user))
#
#         self.battle = Arena.objects.create(
#             first_pokemon=first_pokemon,
#             second_pokemon=second_pokemon)
#
#
# class AfterBattle(BeforeBattle):
#     def __init__(self):
#         super().__init__()
#         self.start_first_hp = 0
#         self.start_second_hp = 0
#
#     def get_start_hp(self):
#         self.start_first_hp = self.battle.first_pokemon.hp
#         self.start_second_hp = self.battle.second_pokemon.hp
#
#     def set_start_hp(self):
#         self.battle.first_pokemon.hp = self.start_first_hp
#         self.battle.second_pokemon.hp = self.start_second_hp
#         self.battle.save()
#
#     def set_battle_result(self, result):
#         self.battle.result = result.name
#         self.battle.save()
#
#
# class Battle(AfterBattle):
#     def __init__(self):
#         super().__init__()
#
#     def is_alive(self, pokemon):
#         return pokemon.hp > 0
#
#     def dammage(self, pokemon):
#         return random.randint(1, pokemon.strength)
#
#     def fight(self):
#         first = self.battle.first_pokemon
#         second = self.battle.second_pokemon
#         while True:
#             if self.is_alive(first):
#                 damage = self.dammage(first)
#                 second.hp -= damage
#                 action = f'{first.name} наносит урон {damage} - у {second.name} остается {second.hp} хп'
#                 Logging.log(self.battle, action)
#                 print(action)
#                 if self.is_alive(second):
#                     damage = self.dammage(second)
#                     first.hp -= self.dammage(second)
#                     action = f'{second.name} наносит урон {damage} - у {first.name} остается {first.hp} хп'
#                     Logging.log(self.battle, action)
#                     print(action)
#                 else:
#                     print(f'{first.name} выйграл')
#                     action = f'{first.name} выйграл'
#                     Logging.log(self.battle, action)
#                     LevelUp.add_experience(first)
#                     self.set_battle_result(first)
#                     self.set_start_hp()
#                     break
#             else:
#                 print(f'{second.name} выйграл')
#                 action = f'{second.name} выйграл'
#                 Logging.log(self.battle, action)
#                 LevelUp.add_experience(second)
#                 self.set_battle_result(second)
#                 self.set_start_hp()
#                 break
#
#
# class ForTask(Battle):
#     def run(self):
#         self.get_users()
#         self.create_battle()
#         self.get_start_hp()
#         self.fight()
