from django.shortcuts import render
from django.contrib import messages
from .forms import contatoForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def contato(request):
    form = contatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            escolaridade = form.cleaned_data['escolaridade']
            mensagem = form.cleaned_data['mensagem']

            print("Mensagem Enviada")
            print(f'Nome: {nome}')
            print(f'email: {email}')
            print(f'escolaridade: {escolaridade}')
            print(f'mensagem: {mensagem}')
            messages.success(request, 'E-mail enviado com sucesso!')
            form = contatoForm()
        else:
            messages.error(request,'Erro ao enviar e-mail.')


    context = {'form':form}
    return render(request, 'contato.html', context)

def produto(request):
    return render(request,'produto.html')
