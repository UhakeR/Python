CUSTOM USER MODEL

cd desktop
mkdir news
cd news
pipenv install django==2.2.5
pipenv shell
django-admin startproject newspaper_project
python manage.py startapp users
python manage.py runserver

# newspaper_project/settings:
	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'users.apps.UsersConfig', # new
	]
	...
	AUTH_USER_MODEL = 'users.CustomUser' # new

# users/models:
	from django.contrib.auth.models import AbstractUser
	from django.db import models

	class CustomUser(AbstractUser):
	    age = models.PositiveIntegerField(null=True, blank=True)

# crea users/forms:
touch users/forms.py

# users/forms:
	from django import forms
	from django.contrib.auth.forms import UserCreationForm, UserChangeForm

	from .models import CustomUser


	class CustomUserCreationForm(UserCreationForm):

	    class Meta(UserCreationForm):
	        model = CustomUser
	        fields = UserCreationForm.Meta.fields + ('age',)


	class CustomUserChangeForm(UserChangeForm):

	    class Meta:
	        model = CustomUser
	        fields = UserChangeForm.Meta.fields

# users/admin:
	from django.contrib import admin
	from django.contrib.auth.admin import UserAdmin

	from .forms import CustomUserCreationForm, CustomUserChangeForm
	from .models import CustomUser


	class CustomUserAdmin(UserAdmin):
	    add_form = CustomUserCreationForm
	    form = CustomUserChangeForm
	    model = CustomUser


	admin.site.register(CustomUser, CustomUserAdmin)

python manage.py makemigrations users
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

# i campi dello user sono visibili tramite list_display in users/admin. Ora li modifichiamo così
# mostra campi come email, username, age e is_staff.
# users/admin:

	from django.contrib import admin
	from django.contrib.auth.admin import UserAdmin

	from .forms import CustomUserCreationForm, CustomUserChangeForm
	from .models import CustomUser


	class CustomUserAdmin(UserAdmin):
	    add_form = CustomUserCreationForm
	    form = CustomUserChangeForm
	    model = CustomUser
	    list_display = ['email', 'username', 'age', 'is_staff', ] # new

# =========================================================

USER AUTHENTICATION

# crea cartella templates e registration
mkdir templates
mkdir templates/registration

# ora diciamo a django che c'è una nuova cartella, updatando DIRS in
# settings:
	TEMPLATES = [
	    {
	        ...
	        'DIRS': [os.path.join(BASE_DIR, 'templates')], # new
	        ...
	    }
	]

# dobbiamo dirgli che sia nel caso di login sia nel caso di logout, in che pagina sei rediretto.
# in entrambi i casi sarò direzionato alla home.
# settings:

	LOGIN_REDIRECT_URL = 'home'
	LOGOUT_REDIRECT_URL = 'home'

# creiamo 4 nuovi template:
touch templates/registration/login.html
touch templates/base.html
touch templates/home.html
touch templates/signup.html

# base.html sarà ereditato da tutti gli altr template nel progetto.
# {% block content %} serve a overridare il contenuto nei template.

# in base.html scriviamo:

	<!DOCTYPE html>
	<html>
	<head>
	  <meta charset="utf-8">
	  <title>{% block title %}Newspaper App{% endblock title %}</title>
	</head>
	<body>
	  <main>
	    {% block content %}
	    {% endblock content %}
	  </main>
	</body>
	</html>

# in home.html scriviamo:

	{% extends 'base.html' %}

	{% block title %}Home{% endblock title %}

	{% block content %}
	{% if user.is_authenticated %}
	  Hi {{ user.username }}!
	  <p><a href="{% url 'logout' %}">Log Out</a></p>
	{% else %}
	  <p>You are not logged in</p>
	  <a href="{% url 'login' %}">Log In</a> |
	  <a href="{% url 'signup' %}">Sign Up</a>
	{% endif %}
	{% endblock content %}

# in registration/login.html scriviamo:

	{% extends 'base.html' %}

	{% block title %}Log In{% endblock title %}

	{% block content %}
	<h2>Log In</h2>
	<form method="post">
	  {% csrf_token %}
	  {{ form.as_p }}
	  <button type="submit">Log In</button>
	</form>
	{% endblock content %}

# in signup.html scriviamo:

	{% extends 'base.html' %}

	{% block title %}Sign Up{% endblock title %}

	{% block content %}
	<h2>Sign Up</h2>
	<form method="post">
	  {% csrf_token %}
	  {{ form.as_p }}
	  <button type="submit">Sign Up</button>
	</form>
	{% endblock content %}

# Dobbiamo aggiornare newspaper_project/urls.py. Vogliamo la home.html come homepage.
# newspaper_project/urls.py:

	from django.contrib import admin
	from django.urls import path, include # new
	from django.views.generic.base import TemplateView # new

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('users/', include('users.urls')), # new
	    path('users/', include('django.contrib.auth.urls')), # new
	    path('', TemplateView.as_view(template_name='home.html'),
	      name='home'), # new  
	]

# creiamo users/urls.py
touch users/urls.py

# users/urls:
	from django.urls import path

	from .views import SignUpView

	urlpatterns = [
	    path('signup/', SignUpView.as_view(), name='signup'),
	]

# l'ultimo step è views.py che contiene la logica del signup form.
# users/views:
	from django.urls import reverse_lazy
	from django.views.generic import CreateView

	from .forms import CustomUserCreationForm


	class SignUpView(CreateView):
	    form_class = CustomUserCreationForm
	    success_url = reverse_lazy('login')
	    template_name = 'signup.html'

# vogliamo inserire email tra i campi da mostrare. Andiamo su users/forms.py
# users/forms.py
	class Meta(UserCreationForm):
	        model = CustomUser
	        fields = ('username', 'email', 'age',) # new

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age',) # new

# ==============================================

BOOTSTRAP

# creiamo l'app pages
python manage.py startapp pages

# updata newsproject_settings.py

	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',
	    'users.apps.UsersConfig',
	    'pages.apps.PagesConfig', # new
	]

# updata newspaper_project/urls. Rimuovi TemplateView.
# newspaper_project/urls:
	from django.contrib import admin
	from django.urls import path, include

	urlpatterns = [
	    path('admin/', admin.site.urls),
	    path('users/', include('users.urls')),
	    path('users/', include('django.contrib.auth.urls')),
	    path('', include('pages.urls')), # new
	]

# crea pages/urls.py
touch pages/urls.py

# pages/urls:
	from django.urls import path

	from .views import HomePageView

	urlpatterns = [
	    path('', HomePageView.as_view(), name='home'),
	]

# pages/views:
	from django.views.generic import TemplateView

	class HomePageView(TemplateView):
	    template_name = 'home.html'

# incolla il codice per il template di bootstrap in
# templates/base:
	<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet"
	    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/\
	    bootstrap.min.css"
	    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81i\
	    uXoPkFOJwJ8ERdknLPMO"
	    crossorigin="anonymous">

	    <title>Hello, world!</title>
	  </head>
	  <body>
	    <h1>Hello, world!</h1>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
	    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4\
	    YfRvH+8abtTE1Pi6jizo"
	    crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
	    integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
	    crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
	    integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
	    crossorigin="anonymous"></script>
	  </body>
	</html>

# idem però con l'aggiunta della navbar
# templates/base:
	<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet"
	    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css"
	    integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO"
	    crossorigin="anonymous">

	    <title>{% block title %}Newspaper App{% endblock title %}</title>
	  </head>
	  <body>
	    <nav class="navbar navbar-expand-md navbar-dark bg-dark mb-4">
	      <a class="navbar-brand" href="{% url 'home' %}">Newspaper</a>
	      <button class="navbar-toggler" type="button" data-toggle="collapse"
	      data-target="#navbarCollapse" aria-controls="navbarCollapse"
	      aria-expanded="false" aria-label="Toggle navigation">
	        <span class="navbar-toggler-icon"></span>
	      </button>
	      <div class="collapse navbar-collapse" id="navbarCollapse">
	        {% if user.is_authenticated %}
	          <ul class="navbar-nav ml-auto">
	            <li class="nav-item">
	              <a class="nav-link dropdown-toggle" href="#" id="userMenu"
	                data-toggle="dropdown" aria-haspopup="true"
	                aria-expanded="false">
	                {{ user.username }}
	              </a>
	              <div class="dropdown-menu dropdown-menu-right"
	                aria-labelledby="userMenu">
	                <a class="dropdown-item"
	                href="{% url 'password_change'%}">Change password</a>
	                <div class="dropdown-divider"></div>
	                <a class="dropdown-item" href="{% url 'logout' %}">
	                Log Out</a>
	              </div>
	            </li>
	          </ul>
	        {% else %}
	          <form class="form-inline ml-auto">
	            <a href="{% url 'login' %}" class="btn btn-outline-secondary">
	            Log In</a>
	            <a href="{% url 'signup' %}" class="btn btn-primary ml-2">
	            Sign up</a>
	          </form>
	        {% endif %}
	      </div>
	    </nav>
	    <div class="container">
	      {% block content %}
	      {% endblock content %}
	    </div>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
	    integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
	    crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js"
	    integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49"
	    crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"
	    integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy"
	    crossorigin="anonymous"></script>
	  </body>
	</html>

# mettiamo un bottoncino figo nella login.
# templates/registration/login.html:

	...
	<button class="btn btn-success ml-2" type="submit">Log In</button>
	...

# usiamo le crispy forms
pipenv install django-crispy-forms==1.8.1

# aggiungila ai settings.
# newspaper_project/settings:

	INSTALLED_APPS = [
	    'django.contrib.admin',
	    'django.contrib.auth',
	    'django.contrib.contenttypes',
	    'django.contrib.sessions',
	    'django.contrib.messages',
	    'django.contrib.staticfiles',

	    # 3rd Party
	    'crispy_forms', # new

	    # Local
	    'users.apps.UsersConfig',
	    'pages.apps.PagesConfig',
	]

# aggiungi la configurazione di crispy ai settings
# newspaper_project/settings:
	CRISPY_TEMPLATE_PACK = 'bootstrap4'

# modifica templates/signup.html:
	{% extends 'base.html' %}

	{% load crispy_forms_tags %}

	{% block title %}Sign Up{% endblock title%}

	{% block content %}
	  <h2>Sign up</h2>
	  <form method="post">
	    {% csrf_token %}
	    {{ form|crispy }}
	    <button type="submit">Sign Up</button>
	  </form>
	{% endblock content %}

# pimpa il bottone signup, sostituendo con questo:
# templates/signup:
	<button class="btn btn-success" type="submit">Sign Up</button>

# ===============================================================

PASSWORD CHANGE AND register

# creo due nuovi template, uno per cambiare la psw, uno per confermare il cambio psw.
touch templates/registration/password_change_form.html
touch templates/registration/password_change_done.html

# templates/registration/password_change_form:
	{% extends 'base.html' %}

	{% block title %}Password Change{% endblock title %}

	{% block content %}
	  <h1>Password change</h1>
	  <p>Please enter your old password, for security's sake, and then enter your
	  new password twice so we can verify you typed it in correctly.</p>

	  <form method="POST">
	    {% csrf_token %}
	    {{ form.as_p }}
	    <input class="btn btn-success" type="submit" value="Change my password">
	  </form>
	{% endblock content %}

# templates/registration/password_change_done:
	{% extends 'base.html' %}

	{% block title %}Password Change Successful{% endblock title %}

	{% block content %}
	    <h1>Password change successful</h1>
	    <p>Your password was changed.</p>
	{% endblock content %}

# ==========================================================

PASSWORD CHANGE AND RESET
# in fondo a newspaper_project/settings aggiungi:
	EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# crea 4 nuovi template:
touch templates/registration/password_reset_form.html
touch templates/registration/password_reset_done.html
touch templates/registration/password_reset_confirm.html
touch templates/registration/password_reset_complete.html

# in templates/registration/password_reset_form.html:

	{% extends 'base.html' %}

	{% block title %}Forgot Your Password?{% endblock title %}

	{% block content %}
	<h1>Forgot your password?</h1>
	<p>Enter your email address below, and we'll email instructions for setting a new one.</p>
	<form method="POST">
	  {% csrf_token %}
	  {{ form.as_p }}
	  <input class="btn btn-success" type="submit" value="Send me instructions!">
	</form>
	{% endblock content %}

# in templates/registration/password_reset_done.html:

	{% extends 'base.html' %}

	{% block title %}Email Sent{% endblock title %}

	{% block content %}
	  <h1>Check your inbox.</h1>
	  <p>We've emailed you instructions for setting your password. You should receive the email shortly!</p>
	{% endblock content %}

# in templates/registration/password_reset_confirm.html:

	{% extends 'base.html' %}

	{% block title %}Enter new password{% endblock title %}

	{% block content %}
	<h1>Set a new password!</h1>
	<form method="POST">
	  {% csrf_token %}
	  {{ form.as_p }}
	  <input class="btn btn-success" type="submit" value="Change my password">
	</form>
	{% endblock content %}

# in templates/registration/password_reset_complete.html:

	{% extends 'base.html' %}

	{% block title %}Password reset complete{% endblock title %}

	{% block content %}
	<h1>Password reset complete</h1>
	<p>Your new password has been set. You can log in now on the
	<a href=
	"{% url 'login' %}">log in page</a>.</p>
	{% endblock content %}

