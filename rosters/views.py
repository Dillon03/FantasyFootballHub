
from django.shortcuts import render, redirect
from .models import FantasyTeam
from .forms import PlayerForm


def home(request):
    teams = FantasyTeam.objects.all()
    return render(request, "rosters/home.html", {"teams": teams})


def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = PlayerForm()

    return render(request, "rosters/add_player.html", {"form": form})
