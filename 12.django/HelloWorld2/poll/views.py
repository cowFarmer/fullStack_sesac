from django.shortcuts import render, get_object_or_404
from .models import Question, Choice


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'poll/question_list.html', {'questions': questions})

def question_detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'poll/question_detail.html', {'question': question})

def question_vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    print(question.choice_set.get())
    pass

def question_results(request, pk):
    pass