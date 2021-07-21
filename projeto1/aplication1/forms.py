from django import forms
from django.forms.fields import CharField, EmailField

class contatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    escolaridade = forms.CharField(label='escolaridade', max_length=100)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
