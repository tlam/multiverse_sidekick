from django.forms import ModelForm
from django.forms import fields
from django.forms.widgets import CheckboxSelectMultiple

from games.models import Game
from heroes.models import Hero


class GameForm(ModelForm):
    class Meta:
        model = Game
        fields = ('villain', 'environment',)

    def __init__(self, num_heroes, is_random, *args, **kwargs):
        super(GameForm, self).__init__(*args, **kwargs)
        self.fields['heroes'] = fields.MultipleChoiceField(required=True, widget=CheckboxSelectMultiple, choices=Hero.choices(num_heroes, is_random))
