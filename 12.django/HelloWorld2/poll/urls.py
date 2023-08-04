from django.urls import path
from . import views


urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:pk>', views.question_detail, name='question_detail'),
    path('<int:pk>/vote', views.question_vote, name='question_vote'),
    path('<int:pk>/results', views.question_results, name='question_results'),
]
