from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("data_visualization/", views.data_visualization, name="data_visualization"),
    path("journal_article/", views.journal_article, name="journal_article"),
    path("questionnaire/", views.questionnaire, name="questionnaire"),
    path("image/", views.image, name="image"),
]
