from django.urls import path

from . import views as vw

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", vw.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", vw.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", vw.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", vw.vote, name="vote"), 
]
