from django.shortcuts import render


def teste(request):
    return render(request, "home_page/homepage.html")