from django.shortcuts import render
from .models import Questions
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse

lst = []
anslist = []
answers = Questions.objects.all()

for i in answers:
    anslist.append(i.answer)

def home(request):
    lst.clear()
    return render(request, 'home.html')

def quiz(request):
    obj = Questions.objects.all()
    paginator = Paginator(obj, 1)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        questions = paginator.page(page)
    except (EmptyPage, InvalidPage):
        questions = paginator.page(paginator.num_pages)

    return render(request, 'quiz.html', {'obj': obj, 'questions': questions})

def result(request):
    score = 0
    print("User Answers:", lst)  # Debugging line
    print("Correct Answers:", anslist)  # Debugging line
    for i in range(len(lst)):
        if lst[i] == anslist[i]:
            score += 1
    print("Final Score:", score)  # Debugging line
    return render(request, 'result.html', {"score": score})

def saveans(request):
    ans = request.GET.get('ans')
    lst.append(ans)
    return HttpResponse('Answer saved')
