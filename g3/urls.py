
from urllib.parse import urlparse
from django.urls import URLPattern
from django.urls import path
from . import views
from django.urls import re_path
from voting.views import vote_on_object
 

app_name = 'g3'
urlpatterns = [
    path('c_micro/', views.c_micro.as_view(), name='c_micro'),
    path('c_anap/', views.c_anap.as_view(), name='c_anap'),
    path('c_anat/', views.c_anat.as_view(), name='c_anat'),
    path('c_biocli/', views.c_biocli.as_view(), name='c_biocli'),
    path('c_embryo/', views.c_embryo.as_view(), name='c_embryo'),
    path('c_immuno/', views.c_immuno.as_view(), name='c_immuno'),
    path('c_parasito/', views.c_parasito.as_view(), name='c_parasito'),
    path('c_pharm/', views.c_pharm.as_view(), name='c_pharm'),
    path('c_physio/', views.c_physio.as_view(), name='c_physio'),
    path('c_physios/', views.c_physios.as_view(), name='c_physios'),
    path('c_radio/', views.c_radio.as_view(), name='c_radio'),
    path('form_anap/', views.form_anap, name='form_anap'),
    path('form_parasi/', views.form_parasi, name='form_parasi'),
    path('form_radio/', views.form_radio, name='form_radio'),
    path('form_physio/', views.form_physio, name='form_physio'),
    path('form_physios/', views.form_physios, name='form_physios'),
    path('form_embryo/', views.form_embryo, name='form_embryo'),
    path('form_micro/', views.form_micro, name='form_micro'),
    path('form_anat/', views.form_anat, name='form_anat'),
    path('form_pharm/', views.form_pharm, name='form_pharm'),
    path('form_biocli/', views.form_biocli, name='form_biocli'),
    path('form_immuno/', views.form_immuno, name='form_immuno'),
    path('anat/', views.index_anat.as_view(), name='index_anat'),
    path('anap/', views.index_anap.as_view(), name='index_anap'),
    path('biocli/', views.index_biocli.as_view(), name='index_biocli'),
    path('radio/', views.index_radio.as_view(), name='index_radio'),
    path('embryo/', views.index_embryo.as_view(), name='index_embryo'),
    path('immuno/', views.index_immuno.as_view(), name='index_immuno'),
    path('parasito/', views.index_parasito.as_view(), name='index_parasito'),
    path('micro/', views.index_micro.as_view(), name='index_micro'),
    path('pharm/', views.index_pharm.as_view(), name='index_pharm'),
    path('physio/', views.index_physio.as_view(), name='index_physio'),
    path('physios/', views.index_physios.as_view(), name='index_physios'),
    path('<int:anapath_id>/anapath/', views.detail_anap, name ='anapath'),
    path('<int:microbiologie_id>/microbiologie/', views.detail_micro, name='microbiologie'),
    path('<int:anatomie_id>/anatomie/', views.detail_anat, name='anatomie'),
    path('<int:pharmacologie_id>/pharmacologie/', views.detail_pharm, name='pharmacologie'),
    path('<int:physiopathologie_id>/physiopathologie/', views.detail_physio, name='physiopathologie'),
    path('<int:physio_speciale_id>/physio_speciale/', views.detail_physios, name='physio_speciale'),
    path('<int:parasito_id>/parasitologie/', views.detail_parasito, name='parasitologie'),
    path('<int:embryologie_id>/embryologie/', views.detail_embryo, name='embryologie'),
    path('<int:radiologie_id>/radiologie/', views.detail_radio, name='radiologie'),
    path('<int:immunologie_id>/immunologie/', views.detail_immuno, name='immunologie'),
    path('<int:biologie_clinique_id>/biologie_clinique/', views.detail_biocli, name='biologie_clinique'),
]