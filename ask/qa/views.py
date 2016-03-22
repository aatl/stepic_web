from django.contrib import auth
# from django.contrib.auth import forms

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.db.models import manager

from django.core.paginator import Paginator, EmptyPage
# from django.db.models import
from django.views.decorators.http import require_POST

from models import Question, Answer, User, models

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from qa.forms import AskForm,AnswerForm, SignupForm, LoginForm


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

    # user1 = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    # user1.last_name = 'Lennon'
    # user1.save()
    # user2 = User.objects.create_user('user1', 'user1@thebeatles.com', 'user1password')
    # user2.last_name = 'Username'
    # user2.save()
    # user3 = User.objects.create_user('user2', 'user2@gmail.com', 'user2password')
    # user3.save()
    # user4 = User.objects.create_user('user3', 'user3@yandex.com', 'qwerty')
    # user4.save()
    # user5 = User.objects.create_user('user4', 'user4@thebeatles.com', 'user4password')
    # user5.save()
    # user6 = User.objects.create_user('user5', 'user5@thebeatles.com', 'johnpassword')
    # user6.save()
    # user7 = User.objects.create_user('petrov', 'petrov@gmail.com', 'petrovpassword')
    # user7.save()
    # user8 = User.objects.create_user('ivanov', 'ivanov@yandex.com', '12345')
    # user8.save()
    # user9 = User.objects.create_user('sidorov', 'sidorov@yahoo.com', '54321')
    # user9.save()
    # user10 = User.objects.create_user('johnson', 'johnson@thebeatles.com', 'asdf')
    # user10.save()

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
    qs = qs.order_by('-id')
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
        # questionPage._user = request.user
    except Question.DoesNotExist:
        raise Http404

    qs = Answer.objects.filter(question = qid)
    page = qs[:]

    return render(request, 'question.html', {
        'question': questionPage,
        'page': page,
        'answerForm': AnswerForm(initial={'question': qid}),
    })


def askHandler(request):
    if request.method == 'POST':
        ask_form = AskForm(request.POST)

        ask_form._user = request.user

        if ask_form.is_valid():
            question = ask_form.save()
            # return HttpResponseRedirect(reverse('questionReverse', args=str(question.id)))
            return HttpResponseRedirect('/question/'+ str(question.id))
    else:
        ask_form = AskForm()
        # ask_form.text = 'get'
    return render(request, 'askFormTemplate.html', {
        'template_form': ask_form,
        'actionReverse': '/ask/',
    })


@require_POST
def answerHandle(request):
    answer = AnswerForm(request.POST)
    answer._user = request.user
    if answer.is_valid():
        answer = answer.save()
        return HttpResponseRedirect('/question/' + str(answer.question_id))

    return HttpResponseRedirect('/question/' + str(answer.get_question()) )



def signupHandler(request):

    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username= username, password= password)
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = SignupForm()

    return render(request, 'signupTemplate.html', {
        'signupForm': form,

    })


def loginHandler(request):

    if request.POST:
        username = request.POST.get('username')
        passwd = request.POST.get('password')

        user = auth.authenticate(username=username, password= passwd)

        # if user is not None and user.is_active():
        auth.login(request, user)
        return HttpResponseRedirect('/')

    form = LoginForm()

    return render(request, 'loginTemplate.html', {
        'loginForm': form,
    })