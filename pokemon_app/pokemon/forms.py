from django.forms import ModelForm, HiddenInput

from .models import Pokemon


class PokemonForm(ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'
        widgets = {'owner': HiddenInput(),
                   'name': HiddenInput(),
                   'portrait': HiddenInput(),
                   'level': HiddenInput(),
                   'experience': HiddenInput(),
                   'hp': HiddenInput(),
                   'ac': HiddenInput(),
                   'strength': HiddenInput(),
                   'dexterity': HiddenInput(),
                   'constitution': HiddenInput(),
                   'win_count': HiddenInput(),
                   'defeat_count': HiddenInput(),
                   }