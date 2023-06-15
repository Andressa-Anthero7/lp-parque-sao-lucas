from django.db.models import Q
from django.shortcuts import render, redirect
from datetime import datetime
from .models import LeadsPsl
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'lp/index.html')


def landingpage_psl(request):
    return render(request, 'lp/lp-psl.html')


def landingpage_form_psl(request):
    if request.method == 'POST':
        nome_leads = request.POST.get('nome_leads')
        email_leads = request.POST.get('email_leads')
        whatsapp_leads = request.POST.get('whatsapp_leads')
        data_recebimento = datetime.now()
        LeadsPsl.objects.create(nome_leads=nome_leads,
                                email=email_leads,
                                whatsapp=whatsapp_leads,
                                data_recebimento=data_recebimento)
        return redirect('pagina-agradecimento')
    else:
        return render(request, 'lp/form-lp-psl.html')


def pagina_agradecimento(request):
    return render(request, 'lp/pagina-agradecimento.html')


@login_required
def dashboard(request):
    leads = LeadsPsl.objects.all().order_by('-data_recebimento')
    busca = request.GET.get('barra-pesquisa')
    if busca:
        leads = LeadsPsl.objects.filter(
            Q(nome_leads__icontains=busca) | Q(whatsapp=busca) | Q(email__icontains=busca) | Q(
                data_recebimento__icontains=busca))
    return render(request, 'lp/dashboard.html', {'leads': leads, 'busca': busca})
