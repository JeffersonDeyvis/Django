<style>
    body{
        background-color:#6f9fe9;
        color: black;
    }
</style>
# Fluxograma

## Roteiro mínimo para Django

### Criando ambiente virtual:
```python
python -m venv venv
```
### Ativando ambiente virtual:
```python
./venv/Scripts/Activate.ps1
```
### Instalando bibliotecas:
```python
pip install django whitenoise gunicorn django-bootstrap4 PyMySQL django-stdimage
```
### Criando requirements.txt:
```python
pip freeze > requirements.txt
```
### Criando Projeto:
```python
django-admin startproject projeto .
```
### Criando Aplicação:
```python
django-admin startapp aplication1
```
### Settings:
```
ALLOWED_HOSTS = ['*']
``` 

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'aplication1',
    'bootstrap4',
    'stdimage',
]
``` 

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
#### configurar data base:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'projeto',
        'USER': 'root',
        'PASSWORD': '******',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
#### configurando staticfiles:
```
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```
### Definindo e configurando as views:

#### definir as funções em ```views.py``` para renderizar o HTML:

```python
def pagina_exemplo(request):
    return render(request,'pagina_exemplo.html')
```

#### criar diretórios:

```/aplications1/static/css```

```/aplications1/static/images```

```/aplications1/static/js```

```/aplications1/templates```

#### criar as páginas HTML, definidas nas views: 

```aplication1/templates/pagina_exemplo.html```

### Definindo as rotas:

#### No arquivo  ``` /settings.urls.py```:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aplication1.urls')),
]
```

#### Em ``` /aplication1``` crie o arquivo ```urls.py```:

``` python
from django.urls import path
from .views import pagina_exemplo ,pagina_exemplo2

urlpatterns = [
    path('', pagina_exemplo,   name='pagina_exemplo'),
    path('pagina_exemplo2/', pagina_exemplo2,   name='pagina_exemplo2'),
]

```
#### No terminal:
```python
pip install MySQL
```
```python
pip freeze > requirements.txt
```
```python
python manage.py migrate
```
#### ainda no terminal... crie o superuser:
```python
python manage.py createsuperuser
```
### Rode a aplicação para ver se está tudo ok com o comando:
```python
python manage.py runserver
```

### isso define o roteiro mínimo para a criação de uma aplicação Django
#### jefferson Deyvis dos Santos Silva