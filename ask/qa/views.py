from django.shortcuts import render
from django.db.models import manager

from django.core.paginator import Paginator, EmptyPage
# from django.db.models import
from models import Question, Answer, User, models

# Create your views here.
from django.http import HttpResponse, Http404


def pagination(request, qs):

    limit = 10
    try:
        pageNum = int(request.GET.get('page', 1))
    except:
        raise Http404


    paginator = Paginator(qs[:], limit)

    try:
        page = paginator.page(pageNum)
    except:
        page = paginator.page(paginator.num_pages)

    return page;



def test(request, *args, **kwargs):
    # author_name = Author.objects.get(pk=1)
    # author_name = Author.



    #
    # return render(request, 'test.html', {
    #     'author': author_name
    # })
    return HttpResponse('OK')




def popularHandle(request, *args, **kwargs):
    qs = Question.objects.order_by('-rating')
    page = pagination(request, qs)
    questionString = '/question/'

    return render(request, 'popular.html', {
        'page': page,
        'questionString': questionString,
    })



def homeHandle(request, *args, **kwargs):
    qs = Question.objects
    qs = qs.order_by('-added_at')
    questionString = '/question/'
    page = pagination(request, qs)

    return render(request, 'home.html', {
        'page': page,
        'questionString': questionString,
    })


def questionsHandler(request, *args, **kwargs):
    qid = int(kwargs['questionId'])

    try:
        questionPage = Question.objects.get(pk = qid)
    except Question.DoesNotExist:
        raise Http404

    qs = Answer.objects.filter(question = qid)
    page = qs[:]

    return render(request, 'question.html', {
        'question': questionPage,
        'page': page,
    })