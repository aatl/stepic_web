from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from qa.models import Question,Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    _user = ''
    #
    # def clean_title(self):
    #     cur_text = self.cleaned_data['title']
    #     return 'cleaned title'
    #
    # def clean_text(self):
    #     cur_text = self.cleaned_data['text']
    #     return 'cleaned text'

    # def __init__(self, user='john', **kwargs):
    #     _user = user
    #     super(AskForm, self).__init__(**kwargs)

    def save(self):
        self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())
    _user = ''

    def save(self):
        question = Question.objects.get(pk = self.cleaned_data['question'])
        self.cleaned_data['question'] = question
        self.cleaned_data['author'] = self._user

        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    def get_question(self):
        return self.cleaned_data['question']




class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        user = User.objects.filter(username = self.cleaned_data['username'])
        if user:
            raise ValidationError('username is used')
        return self.cleaned_data

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

    def get_user(self):
        user = User.objects.get(username = self.cleared_data['username'])
        if not user:
            return False
        if user.password != self.cleared_data['password']:
            return False

        return user