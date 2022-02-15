from datetime import date
import datetime
from django.forms import ValidationError
from django.utils import timezone
from enum import auto, unique
from django.db import models
from django.core.files import File
from django.contrib.auth.models import User
from django.db.models import F

# Create your models here.

class anapath(models.Model): 
    anapath = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField()
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description
  
class comment_anap(models.Model):
    class Meta:
        unique_together = ['user','comments']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.comments

class anatomie(models.Model):
    anatomie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description


class comment_anat(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class biologie_clinique(models.Model):
    bioclinique = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_biocli(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class embryologie(models.Model):
    embryologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_embryo(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class immunologie(models.Model):
    immunologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_immuno(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class microbiologie(models.Model):
    microbiologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_micro(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class parasito(models.Model):
    parasito = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_parasito(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class pharmacologie(models.Model):
    pharmacologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_pharm(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class physio_speciale(models.Model):
    physio_speciale = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_physios(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class physiopathologie(models.Model):
    physiopathologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_physio(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments

class radiologie(models.Model):
    radiologie = models.FileField(upload_to='media/')
    description = models.TextField(default='')
    date = models.DateTimeField(null=True, blank=True)
    nb_vues = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class comment_radio(models.Model):
    class Meta:
        unique_together = ['user','comments','pub_date']

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    comments = models.TextField(default='')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.comments