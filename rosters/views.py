from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FantasyTeam, Player
from .forms import PlayerForm


@login_required
def home(request):
    teams = FantasyTeam.objects.filter(owner=request.user)
    return render(request, "rosters/home.html", {"teams": teams})


@login_required
def add_player(request):
    if request.method == "POST":
        form = PlayerForm(request.POST)
    else:
        form = PlayerForm()

    # Only show teams belonging to the logged-in user
    form.fields["team"].queryset = FantasyTeam.objects.filter(
        owner=request.user
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("home")

    return render(request, "rosters/add_player.html", {"form": form})


@login_required
def manage_roster(request, team_id):
    team = get_object_or_404(
        FantasyTeam,
        id=team_id,
        owner=request.user
    )

    return render(request, "rosters/manage_roster.html", {
        "team": team
    })


@login_required
def edit_player(request, player_id):
    player = get_object_or_404(
        Player,
        id=player_id,
        team__owner=request.user
    )

    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
    else:
        form = PlayerForm(instance=player)

    # Prevent moving players to another user's team
    form.fields["team"].queryset = FantasyTeam.objects.filter(
        owner=request.user
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("manage_roster", team_id=player.team.id)

    return render(request, "rosters/edit_player.html", {
        "form": form,
        "player": player
    })


@login_required
def remove_player(request, player_id):
    player = get_object_or_404(
        Player,
        id=player_id,
        team__owner=request.user
    )

    team_id = player.team.id

    if request.method == "POST":
        player.delete()
        return redirect("manage_roster", team_id=team_id)

    return render(request, "rosters/remove_player.html", {
        "player": player
    })

@login_required
def create_team(request):
    if request.method == "POST":
        team_name = request.POST.get("name", "").strip()

        if team_name:
            FantasyTeam.objects.create(
                name=team_name,
                owner=request.user
            )
            return redirect("home")

    return render(request, "rosters/create_team.html")
