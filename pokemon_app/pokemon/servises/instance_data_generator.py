import random


class Data:
    name_data = ('Пикачу', 'Бульбазавр', 'Чармандер', 'Сквиртл')


class Generator(Data):
    def __init__(self):
        self.name = random.choice(self.name_data)
        self.portrait = f'portrait/{self.name.lower()}.jpeg'

        self.experience = 0

        self.strength = random.randint(8, 12)
        self.constitution = random.randint(8, 12)

        self.hp = self.constitution + random.randint(1, 6)

        self.win_count = 0
        self.defeat_count = 0


# x = Generator()
#
# print(x.name)
# print(x.portrait)
#
# print(x.strength, x.dexterity, x.constitution)