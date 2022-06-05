from django.shortcuts import render
from genshin.models import Character


def index(request):
    characters = Character.objects.order_by('name')[:8]

    context = {
        'characters': characters
    }

    return render(request, 'index.html', context=context)

