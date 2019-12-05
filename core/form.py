from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Treino

class UserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'})
        }
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None



class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'dia_semana': forms.TextInput(attrs={'class':'form-control'}),
            'regiao': forms.SelectMultiple(attrs={'class':'form-control'}),
            'tempo_repaticao': forms.Select(attrs={'class':'form-control'}),
            'intervalo_treinos': forms.Select(attrs={'class':'form-control'}),
            'user': forms.HiddenInput(attrs={'class':'form-control'}),
        }