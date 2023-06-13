from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('parque_sao_lucas/', views.landingpage_psl, name='parque-sao-lucas'),
    path('formulario_parque_sao_lucas/', views.landingpage_form_psl, name='formulario-parque-sao-lucas'),

]
