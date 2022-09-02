from  django.urls import include, path
from django.contrib import admin
from . import views as v1

app_name = 'app01'

urlpatterns = [
    path('tramitacoes', v1.v001_cadastro_tramitacoes, name='cadastro_tramitacoes'),
    path('dadosGeraisDoProcesso', v1.v002_dadosGeraisDoProcesso, name='dadosGeraisDoProcesso'),  
    path('baseAtiva', v1.v008_baseAtiva, name='baseAtiva') ,
    path('inserir-hr', v1.v010_honRecebidos, name="inserir-hon-recebidos"),
    path('honorarios', v1.v011_honorarios, name="honorarios"),
    path('honpericiais', v1.v003_honorariosPericiais, name='incluirHp'), 

]
