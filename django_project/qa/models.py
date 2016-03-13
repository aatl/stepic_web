from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name='question_user')
    likes = models.ManyToManyField(User, related_name='likes_user')



class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = models.ForeignKey(Question, null=False)
    author = models.ForeignKey(User)

