# vuejs-django-jlugao

Tutorial de VueJS com Django segundo o tutorial de João Lugão em Bora falar de Python.

Nesse tutorial João Lugão trabalha com Django e VueJS de forma separada. E ele usar [DRF](http://www.django-rest-framework.org/).

YouTube:

[Bora falar de Python - parte 1](https://www.youtube.com/watch?v=eD6_VzwnIvI)

[Bora falar de Python - parte 2](https://www.youtube.com/watch?v=gqJS99zQf9Y)

## Como desenvolver?

```
git clone https://github.com/rg3915/vuejs-django-jlugao.git
cd vuejs-django-jlugao
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd backend
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Tutorial

Comece criando duas pastas:

```
mkdir backend frontend
```

### Frontend

Iniciando com vue-cli

```
cd frontend
vue init webpack .
? Project name: myproject
? Project description: Exemplo de app com VueJS e Django Rest Framework.
? Install vue-router?: N
```


Instalando tudo

`npm install`


Rodando o projeto

`npm run dev`



### Backend

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework dj-database-url dj-static django-extensions python-decouple
pip freeze > requirements.txt
django-admin.py startproject myproject .
python manage.py startapp core
echo "frontend/node_modules/" >> ../.gitignore
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser
```


## Rodando os projetos

Rode o backend na porta 8000

```
python manage.py runserver
```

Rode o frontend na porta 8080

```
npm run dev
```

Abra a aplicação na porta 8080.
