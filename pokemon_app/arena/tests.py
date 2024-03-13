from django.contrib.auth import get_user_model
from django.test import TestCase

from pokemon.models import Pokemon
from .models import Log, Arena
from .servises.servises import Logging, BeforeBattle, AfterBattle, Battle

User = get_user_model()


class BeforeBattleViewTestCase(TestCase):
    def setUp(self):
        self.user_eugene = User.objects.create(username='eugene')
        self.user_john = User.objects.create(username='john')

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
            owner=self.user_john,
            name='Bulbasaur',
            portrait='portrait/bulbasaur.jpeg',
            experience=950,
            level=1,
            strength=10,
            constitution=10,
            hp=15,
        )

    def test_get_users(self):
        users = BeforeBattle()
        users.get_users()

        self.assertIn(users.first_user, (1, 2))
        self.assertIn(users.second_user, (1, 2))

    def test_create_battle(self):
        battle = BeforeBattle()
        battle.get_users()
        battle.create_battle()

        self.assertIn(battle.battle.first_pokemon.name, ('Pikachu', 'Bulbasaur'))
        self.assertIn(battle.battle.second_pokemon.name, ('Pikachu', 'Bulbasaur'))

    class AfterBattleViewTestCase(TestCase):
        def setUp(self):
            self.user_eugene = User.objects.create(username='eugene')
            self.user_john = User.objects.create(username='john')

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
                owner=self.user_john,
                name='Bulbasaur',
                portrait='portrait/bulbasaur.jpeg',
                experience=950,
                level=1,
                strength=10,
                constitution=10,
                hp=15,
            )

    def test_get_start_hp(self):
        hp = AfterBattle()
        hp.get_users()
        hp.create_battle()
        hp.get_start_hp()

        self.assertEquals(hp.start_first_hp, 15)
        self.assertEquals(hp.start_second_hp, 15)

    def test_set_start_hp(self):
        hp = AfterBattle()
        hp.get_users()
        hp.create_battle()
        hp.get_start_hp()

        hp.battle.first_pokemon.hp = 9
        hp.battle.second_pokemon.hp = 7

        hp.set_start_hp()

        self.assertEquals(hp.battle.first_pokemon.hp, 15)
        self.assertEquals(hp.battle.second_pokemon.hp, 15)

    def test_set_battle_result(self):
        hp = AfterBattle()
        hp.get_users()
        hp.create_battle()
        hp.set_battle_result(hp.battle.second_pokemon)

        self.assertIn(hp.battle.result, ('Pikachu', 'Bulbasaur'))


class BattleViewTestCase(TestCase):

    def setUp(self):
        self.user_eugene = User.objects.create(username='eugene')
        self.user_john = User.objects.create(username='john')

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
            owner=self.user_john,
            name='Bulbasaur',
            portrait='portrait/bulbasaur.jpeg',
            experience=950,
            level=1,
            strength=10,
            constitution=10,
            hp=15,
        )

    def test_fight(self):
        battle = Battle()
        battle.get_users()
        battle.create_battle()
        battle.get_start_hp()
        battle.fight()

        print(battle.battle.result)

        self.assertIn(battle.battle.result, ('Pikachu', 'Bulbasaur'))


class LoggingViewTestCase(TestCase):
    def setUp(self):
        self.user_eugene = User.objects.create(username='eugene')
        self.user_john = User.objects.create(username='john')

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
            owner=self.user_john,
            name='Bulbasaur',
            portrait='portrait/bulbasaur.jpeg',
            experience=950,
            level=1,
            strength=10,
            constitution=10,
            hp=15,
        )

    def test_log(self):
        battle = Battle()
        battle.get_users()
        battle.create_battle()

        log = Logging.log(battle.battle, 'Test action',
        )

        self.assertEquals(log.action, 'Test action')
