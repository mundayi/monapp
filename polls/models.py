from enum import unique
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your models here.

class Question(models.Model):
    question_text = models.TextField(default='', verbose_name='Post')
    pub_date = models.DateTimeField('date published')
 
    def __str__(self):
        return self.question_text
 
 
class Choice(models.Model):
    class Meta:
        unique_together = ['choice_text','voters']

    question = models.ForeignKey(Question, on_delete = models.SET_NULL, null=True, blank=True)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    voters = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.choice_text