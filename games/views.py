from django.contrib import messages
from django.forms.models import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render

from environment.models import Environment
from games.forms import GameForm
from games.models import ActiveHero, Game
from heroes.models import Hero
from villains.models import Villain


def index(request):
    if request.user.is_anonymous():
        games = Game.objects.order_by('-created_at')
    else:
        games = request.user.game_set.order_by('-created_at')
    context = {
        'games': games,
    }
    return render(
        request,
        'games/index.html',
        context,
    )

def create(request):
    num_heroes = int(request.GET.get('num_heroes', 3))
    is_random = 'random' in request.GET

    if request.method == 'POST':
        form = GameForm(num_heroes, False, request.POST)
        if form.is_valid() and not request.user.is_anonymous():
            game = form.save(commit=False)
            game.profile = request.user
            game.villain_hp = game.villain.starting_hp
            game.save()
            heroes = Hero.objects.filter(pk__in=form.cleaned_data['heroes'])
            count = heroes.count()
            for hero in heroes:
                ActiveHero.objects.create(
                    hero=hero,
                    game=game,
                    hp=hero.starting_hp,
                    order=count,
                )
                count -= 1
            return redirect('games:show', game.pk)
            
    else:
        if is_random:
            initial = {
                'environment': Environment.objects.order_by('?')[0],
                'villain': Villain.objects.order_by('?')[0],
            }
        else:
            initial = {}
        form = GameForm(num_heroes, is_random, initial=initial)

    context = {
        'form': form,
    }
    return render(
        request,
        'games/create.html',
        context,
    )


def show(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    if request.method == 'POST':
        villain_hp = request.POST.get('villain')
        game.villain_hp = villain_hp
        total_hero_hp = 0

        for active_hero in game.activehero_set.all():
            hero_hp = int(request.POST.get('hero-%i' % active_hero.hero.pk, 0))
            total_hero_hp += hero_hp
            active_hero.hp = hero_hp
            active_hero.save()

        if not int(villain_hp) or not total_hero_hp:
            game.is_over = True

        game.save()
        messages.success(request, 'Saved')

    context = {
        'game': game,
        'profile': request.user,
    }

    return render(
        request,
        'games/show.html',
        context,
    )
