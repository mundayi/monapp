from django.contrib.auth.models import User
from importlib.metadata import files
from django.core.files import File
from django import forms
from django.forms.forms import Form
from django.forms import fields, models, widgets
from django.db import models
from django.forms import ModelForm
from django.db.models import fields
from django.urls.conf import include
from g3.models import anapath, comment_anap, anatomie, comment_anat, biologie_clinique, comment_biocli, embryologie, comment_embryo, immunologie, comment_immuno, microbiologie, comment_micro, parasito, comment_parasito, pharmacologie, comment_pharm, physio_speciale, comment_physios, physiopathologie, comment_physio, radiologie, comment_radio

  
class comment_anapForm(forms.ModelForm):    
    class Meta:
        model = comment_anap
        fields = ['comments']

class comment_anatForm(forms.ModelForm):
    class Meta:
        model = comment_anat
        fields = ['comments']

class comment_biocliForm(forms.ModelForm):
    class Meta:
        model = comment_biocli
        fields = ['comments']

class comment_embryoForm(forms.ModelForm):
    class Meta:
        model = comment_embryo
        fields = ['comments']

class comment_immunoForm(forms.ModelForm):
    class Meta:
        model = comment_immuno
        fields = ['comments']

class comment_microForm(forms.ModelForm):
    class Meta:
        model = comment_micro
        fields = ['comments']

class comment_parasitoForm(forms.ModelForm):
    class Meta:
        model = comment_parasito
        fields = ['comments']

class comment_pharmForm(forms.ModelForm):
    class Meta:
        model = comment_pharm
        fields = ['comments']


class comment_physiosForm(forms.ModelForm):
    class Meta:
        model = comment_physios
        fields = ['comments']

class comment_radioForm(forms.ModelForm):
    class Meta:
        model = comment_radio
        fields = ['comments']

class comment_physioForm(forms.ModelForm):
    class Meta:
        model = comment_physio
        fields = ['comments']