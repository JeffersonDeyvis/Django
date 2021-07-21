<style>
    body{
        background-color:#6f9fe9;
        color: black;
    }
</style>
## Roteiro específico para Django

### use o django shell a qualquer momento para estudar os dicionários

```python
python manage.py shell
```

### formulários:

### Temos que criar, dentro de ```aplication1``` um arquivo ```forms.py```

```python
from django import forms
from django.forms.fields import CharField, EmailField

class contatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    escolaridade = forms.CharField(label='escolaridade', max_length=100)
    mensagem = forms.CharField(label='mensagem', widget=forms.Textarea())
```
### chame o arquivo ```forms.py``` dentro do arquivo ```views.py```
```python
from .forms import contatoForm


def contato(request):
    form = contatoForm()
    context = {
        'form' : form
    }
    return render(request,'contato.html', context )
```