from django.forms.models import modelformset_factory
from django.shortcuts import render

from games.forms import GameForm


def create(request):
    num_heroes = int(request.GET.get('num_heroes', 3))

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid() and not request.user.is_anonymous():
            game = form.save(commit=False)
            game.profile = request.user
            game.save()
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
