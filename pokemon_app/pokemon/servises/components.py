import random
from dataclasses import dataclass


# Сущность

class Entity:
    pass


# Компоненты
@dataclass
class Name:
    name: str = None

    def give_name(self, name):
        self.name = name
        return self.name

    def random_choice_name(self, name_list):
        self.name = random.choice(name_list)
        return self.name


@dataclass
class Experience:
    experience: int = 0

    @staticmethod
    def add_experience(creature, exp):
        creature.experience += exp
        creature.save()
        return creature.experience


@dataclass
class Level:
    level: int = 1

    @staticmethod
    def add_level(creature):
        creature.level += 1
        creature.save()
        return creature.level

    @staticmethod
    def check_level(creature):
        return creature.experience - (creature.level * 1000) + 100 >= 0




@dataclass
class Portrait:
    portrait: str = ''


@dataclass
class Health:
    constitution: int = None
    min: int = None
    max: int = None
    health: int = None

    @staticmethod
    def is_alive(creature):
        return creature.hp > 0

    @staticmethod
    def apply_damage(creature, damage):
        creature.hp -= damage
        return creature.hp

    def __post_init__(self):
        if self.min and self.max:
            self.health = self.constitution + random.randint(self.min, self.max)


@dataclass
class Constitution:
    min: int = None
    max: int = None
    constitution: int = None

    @staticmethod
    def add_constitution(creature):
        creature.constitution += 1

    def __post_init__(self):
        if self.min and self.max:
            self.constitution = random.randint(self.min, self.max)


@dataclass
class Strength:
    min: int = None
    max: int = None
    strength: int = None

    @staticmethod
    def damage(creature):
        return random.randint(1, creature.strength)

    @staticmethod
    def add_strength(creature):
        creature.strength += 1

    def __post_init__(self):
        if self.min and self.max:
            self.strength = random.randint(self.min, self.max)
