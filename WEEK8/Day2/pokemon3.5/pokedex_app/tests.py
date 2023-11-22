from django.test import TestCase
from django.core.exceptions import ValidationError

from .models import Pokemon

class pokemon_test(TestCase):

    def test_01_create_pokemon_instance(self):
        new_pokemon = Pokemon(name='Ditto', description='I copy you.')

        try:
            new_pokemon.full_clean()
            self.assertIsNotNone(new_pokemon)
        except ValidationError as e:
            print(e.message_dict)
            self.fail()

    def test_02_create_pokemon_with_incorrect_name_format_capitalize_name(self):
        new_pokemon = Pokemon(name='Squirtle', description="who knows what's going on.")

        try: 
            new_pokemon.full_clean()
            self.fail()
            
        
        except ValidationError as e:
            self.assertTrue('Improper name format' in e.message_dict['name'])
            print(e.message_dict)
            # self.fail()

# Create your tests here.
