from random import choice
from select import select
from datetime import datetime
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import F
from .models import Question, Choice
from polls.forms import QuestionForm
from django.utils import timezone
from django.urls import re_path
from .models import Choice

# Get questions and display them 
 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:1]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
 
# Show specific question and choices
 
 
def detail(request, question_id):
    try:
        question = Question.objects.get(pk = question_id)
    except Question.DoesNotExist:
        raise Http404("Il n'y a aucune publication pour le moment.")
    return render(request, 'polls/detail.html', {'question': question})
 
# Get question and display results
 
 
def results(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})
 
# Vote for a question choice

@permission_required('polls.add_choice')
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Aucun choix n'a été fait.",
        })
    else:
        a, b =Choice.objects.get_or_create(voters=request.user)
        if not b:
            selected_choice.votes = F('votes') + 0
        else:
            selected_choice.votes = F('votes') + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))

@login_required
def display(request):
    if not request.user.email.endswith('Qx@gmail.com'):
        return redirect('/accounts/login/?next=%s' % request.path)
    if request.method == 'POST':
        texte = QuestionForm(request.POST)
        if texte.is_valid():
            c = texte.save(commit=False)
            c.pub_date = datetime.now()
            c.save()

            return HttpResponseRedirect('/polls/')

    else:
        texte = QuestionForm()


    return render(request, 'polls/form_texte.html', locals())