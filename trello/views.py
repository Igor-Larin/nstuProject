from django.shortcuts import render
# Create your views here.


def landing(request, name):
    html_path = 'trello/' + name + '.html'
    return render(request, html_path)