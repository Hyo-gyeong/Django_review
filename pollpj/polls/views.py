from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice

# Create your views here.
def index(request):
    q_list = Question.objects.order_by('pub_date')
    return render(request, 'index.html', {'q_list': q_list})

def detail(request, pk):
    pick = get_object_or_404(Question, pk = pk)
    return render(request, 'detail.html', {'detail':pick})

# def create(request, detail_id):
#     if request.method == 'POST':
#         option = Choice()
#         option.choice_text = request.POST['option']
#         option.save()
#         return redirect('/detail/' + str(option.id))
#     else:
#         return render(request, 'create.html')

def results(request, detail_id):
    question = get_object_or_404(Question, pk = detail_id)
    return render(request, 'results.html', {'rslt':question})

def vote(request, detail_id):
    question = get_object_or_404(Question, pk = detail_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {'question':question, 'error_message':"You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))