
from django.db import models
from django.contrib.auth.models import User


class FantasyTeam(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = [
        ("QB", "Quarterback"),
        ("RB", "Running Back"),
        ("WR", "Wide Receiver"),
        ("TE", "Tight End"),
        ("K", "Kicker"),
        ("DEF", "Defense"),
    ]

    team = models.ForeignKey(
        FantasyTeam, on_delete=models.CASCADE, related_name="players"
    )
    name = models.CharField(max_length=100)
    nfl_team = models.CharField(max_length=50)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    is_starter = models.BooleanField(default=False)

    def __str__(self):
        return self.name
