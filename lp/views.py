from django.shortcuts import render, redirect
from datetime import datetime
from .models import LeadsPsl
from .whatsapp import notificacao


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
        leads = LeadsPsl.objects.last()
        account_sid = 'ACc4b4a408cd71392b6e1240e43319dade'
        auth_token = '2313858665f1d7d814dc5e8a6efbec4a'

        notificacao(leads.pk, account_sid, auth_token)
        return redirect('pagina-agradecimento')
    else:
        return render(request, 'lp/form-lp-psl.html')


def pagina_agradecimento(request):
    return render(request, 'lp/pagina-agradecimento.html')


def dashboard(request):
    leads = LeadsPsl.objects.all()
    return render(request, 'lp/dashboard.html', {'leads': leads})
