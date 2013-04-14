from django.forms.models import modelformset_factory
from django.shortcuts import render

from games.forms import GameForm
from games.models import ActiveHero
from heroes.models import Hero


def create(request):
    num_heroes = int(request.GET.get('num_heroes', 3))

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid() and not request.user.is_anonymous():
            game = form.save(commit=False)
            game.profile = request.user
            game.save()
            heroes = Hero.objects.filter(pk__in=form.cleaned_data['heroes'])
            for hero in heroes:
                ActiveHero.objects.create(
                    hero=hero,
                    game=game,
                    hp=hero.starting_hp,
                )
            
    else:
        form = GameForm()

    context = {
        'form': form,
    }
    return render(
        request,
        'games/create.html',
        context,
    )
