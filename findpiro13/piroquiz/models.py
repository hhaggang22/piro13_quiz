from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_title=models.CharField(max_length=800, verbose_name='퀴즈제목')

class CreateQuiz(models.Model):
    title = models.CharField(max_length = 255, verbose_name='제목')






