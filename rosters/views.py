from django.shortcuts import render, redirect, get_object_or_404
from .models import FantasyTeam, Player
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

def manage_roster(request, team_id):
    team = get_object_or_404(FantasyTeam, id=team_id)

    return render(request, 'rosters/manage_roster.html', {
        'team': team
    })

def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)

    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)

        if form.is_valid():
            form.save()
            return redirect("manage_roster", team_id=player.team.id)
    else:
        form = PlayerForm(instance=player)

    return render(request, "rosters/edit_player.html", {
        "form": form,
        "player": player
    })

def remove_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    team_id = player.team.id

    if request.method == "POST":
        player.delete()
        return redirect("manage_roster", team_id=team_id)

    return render(request, "rosters/remove_player.html", {
        "player": player
    })