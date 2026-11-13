from django import forms
from .models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["team", "name", "nfl_team", "position", "is_starter"]
