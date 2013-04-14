from django.forms import ModelForm
from django.forms import fields
from django.forms.widgets import CheckboxSelectMultiple

from games.models import Game
from heroes.models import Hero


class GameForm(ModelForm):
    heroes = fields.MultipleChoiceField(required=True,
        widget=CheckboxSelectMultiple, choices=Hero.choices())

    class Meta:
        model = Game
        fields = ('villain', 'environment',)
