# Generated by Django 4.2.2 on 2023-06-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeadsPsl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_leads', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=13)),
                ('data_recebimento', models.CharField(max_length=50)),
            ],
        ),
    ]
