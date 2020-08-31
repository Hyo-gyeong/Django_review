from django.shortcuts import render, redirect
from .models import Portfolio
from .forms import NewPofol
from django.utils import timezone

def portfolio(request):
    p = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'blogs':p})

def new(request):
    if request.method == 'POST':
        portfolio = NewPofol(request.POST, request.FILES)
        if portfolio.is_valid:
            p = portfolio.save(commit=False)
            p.date = timezone.datetime.now()
            p.save()
            return redirect('/portfolio/')
    else:
        form = NewPofol()
        return render(request, 'new.html', {'form':form})
        
        