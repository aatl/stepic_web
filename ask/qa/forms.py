from django import forms
from django.contrib.auth.models import User

from qa.models import Question,Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    _user = 'john'
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
        self.cleaned_data['author'] = User.objects.get(pk=1)
        question = Question(**self.cleaned_data)
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput())

    def save(self):
        self.cleaned_data['question'] = Question.objects.get(pk = self.cleaned_data['question'])
        self.cleaned_data['author'] = User.objects.get(pk=1)

        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer

    def get_question(self):
        return self.cleaned_data['question']