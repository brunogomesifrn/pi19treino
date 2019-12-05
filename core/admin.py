from django.contrib import admin
from .models import Regiao_corporal, Tempo_repeticao, Intervalo_treinos, Treino
# Register your models here.

admin.site.register(Regiao_corporal)
admin.site.register(Tempo_repeticao)
admin.site.register(Intervalo_treinos)
admin.site.register(Treino)