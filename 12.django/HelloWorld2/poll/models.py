from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.title}'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.choice_text}'