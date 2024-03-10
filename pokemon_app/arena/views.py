from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView

from .models import Arena, Log
from .servises.servises import ForTask


class ArenaView(ListView):
    template_name = 'arena/arena.html'
    context_object_name = 'result'

    def get_queryset(self):
        return Arena.objects.all()


def show_battle_result(request, battle_id):
    result = get_object_or_404(Arena, pk=battle_id)
    log = Log.objects.filter(battle_id=battle_id)

    context = {
        'result': result,
        'log': log,
    }

    return render(request, 'arena/battle_result.html', context=context)


def battle_test(request):

    test = ForTask()
    test.run()


    return render(request, 'arena/battle.html', {'create': 'x'})
