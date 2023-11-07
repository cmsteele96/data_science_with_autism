from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def data_visualization(request):
    return render(request, "data_visualization.html")


def journal_article(request):
    return render(request, "journal_article.html")


def questionnaire(request):
    return render(request, "questionnaire.html")


def image(request):
    return render(request, "image.html")
