# djando-todoapp
### Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

### General Info
Just another todo app using Django.
[See on Heroku](https://todoapp--django.herokuapp.com/)

### Technologies
* Python 3.8.2
* Django 3.0.7

### Development Setup

Clone the repo

`$ git clone https://github.com/rafius97/django-todoapp.git`

`$ cd django-todoapp`

Configure virtual enviroment with pyenv [See installation](https://github.com/pyenv/pyenv-virtualenv#installation)

`$ pyenv virtualenv 3.8.2 django-todoapp`

`$ pyenv activate django-todoapp`

Install requirements

`$ pip install -r requirements.txt`

Configure the enviroment variable for development

`$ export DJANGO_DEBUG=True`

Run migrate commands

`$ python manage.py makemigrations`

`$ python manage.py migrate`

Run the app server

`$ python manage.py runserver`
