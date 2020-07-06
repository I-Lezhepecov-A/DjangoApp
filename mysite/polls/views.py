from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    lastest_question_list= Question.objects.order_by('-pub_date')[:5]
    context = {
        'lastest_question_list':lastest_question_list
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question=Questionobjects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/index.html', {'question': question})


def results(request, question_id):
    response="You're lookind at the results of question %s."
    return HttpResponse (response % question_id)

def vote(request, question_id):
    return HttpResponse ("You're voting on question %s." %question_id)
