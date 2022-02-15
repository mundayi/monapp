from django.urls import path
from . import views
from django.urls import re_path
from .models import Choice


app_name = 'polls'
urlpatterns = [
    path('form_texte/', views.display, name='form_texte'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name ='detail'),
    path('<int:question_id>/results/', views.results, name ='results'),
    path('<int:question_id>/vote/', views.vote, name ='vote'),
]
