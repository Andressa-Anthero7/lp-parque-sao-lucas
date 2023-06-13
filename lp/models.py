from django.db import models


# Create your models here.

class LeadsPsl(models.Model):
    nome_leads = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    whatsapp = models.CharField(max_length=13)
    data_recebimento = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_leads
