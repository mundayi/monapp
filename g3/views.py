from datetime import datetime
from django import http
from django import template
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required, login_required
from django.template import context, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import F
from importlib.metadata import files
from django.core.files import File
from django import forms
from django.views.generic import ListView, DetailView
from django.forms.forms import Form
from django.forms import fields, models
from django.db import models
from django.forms import ModelForm, forms
from g3.forms import comment_anapForm, comment_anatForm, comment_biocliForm, comment_embryoForm, comment_immunoForm, comment_parasitoForm, comment_pharmForm, comment_physiosForm, comment_radioForm, comment_physioForm, comment_microForm
from . models import anapath, comment_anap, anatomie, comment_anat, biologie_clinique, comment_biocli, comment_micro, embryologie, comment_embryo, immunologie, comment_immuno, microbiologie, comment_immuno, parasito, comment_parasito, pharmacologie, comment_pharm, physio_speciale, comment_physios, physiopathologie, comment_physio, radiologie, comment_radio
from django.urls import re_path
from django.forms import modelformset_factory
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin

# Get questions and display them 

class c_anap(ListView):
    model = comment_anap
    context_object_name = "anap"
    template_name = "g3/c_anap.html"
    queryset = comment_anap.objects.order_by("-pub_date")
    paginate_by = 6

class c_anat(ListView):
    model = comment_anat
    context_object_name = 'anat'
    template_name = "g3/c_anat.html"
    queryset = comment_anat.objects.order_by("-pub_date")
    paginate_by = 6

class c_biocli(ListView):
    model = comment_biocli
    context_object_name = 'biocli'
    template_name = "g3/c_biocli.html"
    queryset = comment_biocli.objects.order_by("-pub_date")
    paginate_by = 6

class c_embryo(ListView):
    model = comment_embryo
    context_object_name = 'embryo'
    template_name = "g3/c_embryo.html"
    queryset = comment_embryo.objects.order_by("-pub_date")
    paginate_by = 6

class c_immuno(ListView):
    model = comment_immuno
    context_object_name = 'immuno'
    template_name = "g3/c_immuno.html"
    queryset = comment_immuno.objects.order_by("-pub_date")
    paginate_by = 6

class c_parasito(ListView):
    model = comment_parasito
    context_object_name = 'parasito'
    template_name = "g3/c_parasito.html"
    queryset = comment_parasito.objects.order_by("-pub_date")
    paginate_by = 6

class c_pharm(ListView):
    model = comment_pharm
    context_object_name = 'pharm'
    template_name = "g3/c_pharm.html"
    queryset = comment_pharm.objects.order_by("-pub_date")
    paginate_by = 6

class c_physio(ListView):
    model = comment_physio
    context_object_name = 'physio'
    template_name = "g3/c_physio.html"
    queryset = comment_physio.objects.order_by("-pub_date")
    paginate_by = 6

class c_physios(ListView):
    model = comment_physios
    context_object_name = 'physios'
    template_name = "g3/c_physios.html"
    queryset = comment_physios.objects.order_by("-pub_date")
    paginate_by = 6

class c_radio(ListView):
    model = comment_radio
    context_object_name = 'radio'
    template_name = "g3/c_radio.html"
    queryset = comment_radio.objects.order_by("-pub_date")
    paginate_by = 6

class c_micro(ListView):
    model = comment_micro
    context_object_name ='micro'
    template_name = 'g3/c_micro.html'
    queryset = comment_micro.objects.order_by("-pub_date")
    paginate_by = 6

class index_anap(ListView):
    model = anapath
    context_object_name = 'anapath_list'
    template_name = "g3/index_anap.html"
    paginate_by = 9
    queryset = anapath.objects.order_by('-date')


class index_anat(ListView):
    model = anatomie
    context_object_name = 'anatomie_list'
    template_name = "g3/index_anat.html"
    paginate_by = 9
    queryset = anatomie.objects.order_by('-date')

class index_pharm(ListView):
    model = pharmacologie
    context_object_name = 'pharmacologie_list'
    template_name = "g3/index_pharm.html"
    paginate_by = 9
    queryset = pharmacologie.objects.order_by('-date')

class index_physio(ListView):
    model = physiopathologie
    context_object_name = 'physiopathologie_list'
    template_name = "g3/index_physio.html"
    paginate_by = 9
    queryset = physiopathologie.objects.order_by('-date')

class index_radio(ListView):
    model = radiologie
    context_object_name = 'radiologie_list'
    template_name = "g3/index_radio.html"
    paginate_by = 9
    queryset = radiologie.objects.order_by('-date')

class index_physios(ListView):
    model = physio_speciale
    context_object_name = 'physio_speciale_list'
    template_name = "g3/index_physios.html"
    paginate_by = 9
    queryset = physio_speciale.objects.order_by('-date')

class index_immuno(ListView):
    model = immunologie
    context_object_name = 'immunologie_list'
    template_name = "g3/index_immuno.html"
    paginate_by = 9
    queryset = immunologie.objects.order_by('-date')

class index_parasito(ListView):
    model = parasito
    context_object_name = 'parasito_list'
    template_name = "g3/index_parasito.html"
    paginate_by = 9
    queryset = parasito.objects.order_by('-date')

class index_embryo(ListView):
    model = embryologie
    context_object_name = 'embryologie_list'
    template_name = "g3/index_embryo.html"
    paginate_by = 9
    queryset = embryologie.objects.order_by('-date')

class index_biocli(ListView):
    model = biologie_clinique
    context_object_name = 'biologie_clinique_list'
    template_name = "g3/index_biocli.html"
    paginate_by = 9
    queryset = biologie_clinique.objects.order_by('-date')

class index_micro(ListView):
    model = microbiologie
    context_object_name = 'microbiologie_list'
    template_name = "g3/index_micro.html"
    paginate_by = 9
    queryset = microbiologie.objects.order_by('-date')

# Show specific question and choices

def detail_anap(request, anapath_id):
    try:
        Anapath = anapath.objects.get(pk=anapath_id)
        if Anapath:
            Anapath.nb_vues = F('nb_vues') + 1
            Anapath.save()
    except anapath.DoesNotExist:
        raise Http404("Anapath videos do not exist")

    return render(request, 'g3/detail_anap.html', context = {'Anapath':Anapath})

def detail_anat(request, anatomie_id):
    try:
        Anatomie = anatomie.objects.get(pk=anatomie_id)
        if Anatomie:
            Anatomie.nb_vues = F('nb_vues') + 1
            Anatomie.save()
    except anatomie.DoesNotExist:
        raise Http404("Anatomie videos do not exist")

    return render(request, 'g3/detail_anat.html', context = {'Anatomie': Anatomie})

def detail_pharm(request, pharmacologie_id):
    try:
        Pharmacologie = pharmacologie.objects.get(pk=pharmacologie_id)
        if Pharmacologie:
            Pharmacologie.nb_vues = F('nb_vues') + 1
            Pharmacologie.save()
    except pharmacologie.DoesNotExist:
        raise Http404("Pharmacologie videos do not exist")

    return render(request, 'g3/detail_pharm.html', context = {'Pharmacologie':Pharmacologie})


def detail_physio(request, physiopathologie_id):
    try:
        Physiopathologie = physiopathologie.objects.get(pk=physiopathologie_id)
        if Physiopathologie:
            Physiopathologie.nb_vues = F('nb_vues') + 1
            Physiopathologie.save()
    except physiopathologie.DoesNotExist:
        raise Http404("Physiopathologie videos do not exist")

    return render(request, 'g3/detail_physio.html', context = {'Physiopathologie':Physiopathologie})


def detail_physios(request, physio_speciale_id):
    try:
        Physio_speciale = physio_speciale.objects.get(pk=physio_speciale_id)
        if Physio_speciale:
            Physio_speciale.nb_vues = F('nb_vues') + 1
            Physio_speciale.save()
    except physio_speciale.DoesNotExist:
        raise Http404("Physio_speciale videos do not exist")

    return render(request, 'g3/detail_physios.html', context = {'Physio_speciale':Physio_speciale})


def detail_parasito(request,  parasito_id):
    try:
        Parasito = parasito.objects.get(pk=parasito_id)
        if Parasito:
            Parasito.nb_vues = F('nb_vues') + 1
            Parasito.save()
    except parasito.DoesNotExist:
        raise Http404("Parasito videos do not exist")

    return render(request, 'g3/detail_parasito.html', context = {'Parasito':Parasito})


def detail_embryo(request,  embryologie_id):
    try:
        Embryologie = embryologie.objects.get(pk=embryologie_id)
        if Embryologie:
            Embryologie.nb_vues = F('nb_vues') + 1
            Embryologie.save()
    except embryologie.DoesNotExist:
        raise Http404("Embryologie videos do not exist")

    return render(request, 'g3/detail_embryo.html', context = {'Embryologie':Embryologie})


def detail_radio(request, radiologie_id):
    try:
        Radiologie = radiologie.objects.get(pk=radiologie_id)
        if Radiologie:
            Radiologie.nb_vues = F('nb_vues') + 1
            Radiologie.save()
    except radiologie.DoesNotExist:
        raise Http404("Radiologie videos do not exist")

    return render(request, 'g3/detail_radio.html', context = {'Radiologie':Radiologie})


def detail_immuno(request, immunologie_id):
    try:
        Immunologie = immunologie.objects.get(pk=immunologie_id)
        if Immunologie:
            Immunologie.nb_vues = F('nb_vues') + 1
            Immunologie.save()
    except immunologie.DoesNotExist:
        raise Http404("Immunologie videos do not exist")

    return render(request, 'g3/detail_immuno.html', context = {'Immunologie':Immunologie})

def detail_micro(request, microbiologie_id):
    try:
        Microbiologie = microbiologie.objects.get(pk=microbiologie_id)
        if Microbiologie:
            Microbiologie.nb_vues = F('nb_vues') + 1
            Microbiologie.save()
    except microbiologie.DoesNotExist:
        raise Http404("Microbiologie videos do not exist")

    return render(request, 'g3/detail_micro.html', context = {'Microbiologie':Microbiologie})


def detail_biocli(request, biologie_clinique_id):
    try:
        Biologie_clinique = biologie_clinique.objects.get(pk=biologie_clinique_id)
        if Biologie_clinique:
            Biologie_clinique.nb_vues = F('nb_vues') + 1
            Biologie_clinique.save()
    except biologie_clinique.DoesNotExist:
        raise Http404("Biologie_clinique videos do not exist")
   
    return render(request, 'g3/detail_biocli.html', context = {'Biologie_clinique':Biologie_clinique})
 
# Get question and display results
 
# Vote for a question choice
@login_required
def form_anat(request):
    if request.method == 'POST':
        anat = comment_anatForm(request.POST, request.FILES)
        if anat.is_valid():
            c = anat.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_anat/')
    else:
        anat = comment_anatForm()

    return render(request, 'g3/form_anat.html', locals())

@login_required
def form_anap(request):
    if request.method == 'POST':
        anap = comment_anapForm(request.POST, request.FILES)
        if anap.is_valid():
            c = anap.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()


            return HttpResponseRedirect('/g3/c_anap/')
    else:
        anap = comment_anapForm()

    return render(request, 'g3/form_anap.html', locals())

@login_required
def form_immuno(request):
    if request.method == 'POST':
        immuno = comment_immunoForm(request.POST, request.FILES)
        if immuno.is_valid():
            c = immuno.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_immuno/')
    else:
        immuno = comment_immunoForm()

    return render(request, 'g3/form_immuno.html', locals())

@login_required
def form_radio(request):
    if request.method == 'POST':
        radio = comment_radioForm(request.POST, request.FILES)
        if radio.is_valid():
            c = radio.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_radio/')
    else:
        radio = comment_radioForm()

    return render(request, 'g3/form_radio.html', locals())

@login_required
def form_biocli(request):
    if request.method == 'POST':
        biocli = comment_biocliForm(request.POST, request.FILES)
        if biocli.is_valid():
            c = biocli.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_biocli/')
    else:
        biocli = comment_biocliForm()

    return render(request, 'g3/form_biocli.html', locals())

@login_required
def form_embryo(request):
    if request.method == 'POST':
        embryo = comment_embryoForm(request.POST, request.FILES)
        if embryo.is_valid():
            c = embryo.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_embryo/')
    else:
        embryo = comment_embryoForm()

    return render(request, 'g3/form_embryo.html', locals())

@login_required
def form_micro(request):
    if request.method == 'POST':
        micro = comment_microForm(request.POST, request.FILES)
        if micro.is_valid():
            c = micro.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_micro/')
    else:
        micro = comment_microForm()

    return render(request, 'g3/form_micro.html', locals())

@login_required
def form_parasi(request):
    if request.method == 'POST':
        parasi = comment_parasitoForm(request.POST, request.FILES)
        if parasi.is_valid():
            c = parasi.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_parasito/')
    else:
        parasi = comment_parasitoForm()

    return render(request, 'g3/form_parasi.html', locals())

@login_required
def form_pharm(request):
    if request.method == 'POST':
        pharm = comment_pharmForm(request.POST, request.FILES)
        if pharm.is_valid():
            c = pharm.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_pharm/')
    else:
        pharm = comment_pharmForm()

    return render(request, 'g3/form_pharm.html', locals())

@login_required
def form_physio(request):
    if request.method == 'POST':
        physio = comment_physioForm(request.POST, request.FILES)
        if physio.is_valid():
            c = physio.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_physio/')
    else:
        physio = comment_physioForm()

    return render(request, 'g3/form_physio.html', locals())

@login_required
def form_physios(request):
    if request.method == 'POST':
        physios = comment_physiosForm(request.POST, request.FILES)
        if physios.is_valid():
            c = physios.save(commit=False)
            c.user = request.user
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/g3/c_physios/')
    else:
        physios = comment_physiosForm()
    
    return render(request, 'g3/form_physios.html', locals())