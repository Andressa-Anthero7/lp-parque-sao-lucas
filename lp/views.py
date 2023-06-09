from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'lp/index.html')


def landingpage_psl(request):
    return render(request, 'lp/lp-psl.html')
