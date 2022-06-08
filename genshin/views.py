from django.shortcuts import render
from genshin.models import Character, Region
from django.views.generic import ListView, DetailView


def index(request):
    characters = Character.objects.order_by('name')[:3]

    context = {
        'characters': characters
    }

    return render(request, 'index.html', context=context)


class GenshinListView(ListView):
    model = Character

    context_object_name = 'genshin_list'
    template_name = 'genshin/list.html'


class GenshinDetailView(DetailView):
    model = Character

    context_object_name = 'character_detail'
    template_name = 'genshin/detail.html'


class RegionListView(ListView):
    model = Region

    context_object_name = 'region_list'
    template_name = 'genshin/region.html'


class RegionDetailView(DetailView):
    model = Region

    context_object_name = 'region_detail'
    template_name = 'genshin/region_detail.html'
