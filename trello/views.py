from django.shortcuts import render
from trello.models import *
# Create your views here.


def landing(request):
    return render(request, 'trello/trello.html')


def registration(request):
    return render(request, 'trello/registration.html')


def main(request):
    tasks = []
    cards = list(Card.objects.values_list('name', flat=True))
    card_ids = list(Card.objects.values_list('id', flat=True))
    for i in card_ids:
        tasks.append(list(Task.objects.values_list('text', flat=True).filter(card_id=i)))
        card_ids[i - 1] = i - 1
    content = {
        'card_ids': card_ids,
        'cards': cards,
        'tasks': tasks
    }
    return render(request, 'trello/main.html', content)
