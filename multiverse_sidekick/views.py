from django.shortcuts import render

from heroes.models import Hero


def home(request):
    max_heroes = Hero.objects.count()
    context = {
        'max_heroes': range(1, max_heroes-1),
    }
    print context
    return render(
        request,
        'home/index.html',
        context,
    )
