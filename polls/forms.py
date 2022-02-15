from django import forms
from django.forms.forms import Form
from django.forms import fields, models, widgets
from django.db import models
from django.forms import ModelForm
from django.db.models import fields
from django.urls.conf import include
from polls.models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model =Question
        fields = ['question_text']