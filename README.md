![contributor](https://img.shields.io/github/contributors/0xricoard/Django-App?color=red) ![size](https://img.shields.io/github/repo-size/0xricoard/Django-App?color=red) ![py version](https://img.shields.io/badge/python-v_3.11.5-blue)
![django version](https://img.shields.io/badge/django-v_4.2.5-green)
![tailwind version](https://img.shields.io/badge/tailwind-v_3.6.0-blue)


# Estimasi Harga Mobil Bekas

Website ini digunakan untuk memperkirakan harga mobil bekas dari spesifikasi mobil yang telah disebutkan.

Website ini dibuat dari bahasa [Python](https://www.python.org/) dengan pemanfaatan [Django](https://www.djangoproject.com/) untuk bisa dijalankan di website, juga menggunakan framework css yaitu [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/index.html).

## Table of Content
- [Estimasi Harga Mobil Bekas](#estimasi-harga-mobil-bekas)
  - [Table of Content](#table-of-content)
  - [Instalasi](#instalasi)
    - [1. Menyiapkan Virtual Environment](#1-menyiapkan-virtual-environment)
    - [2. Masuk Kedalam Virtual Environment](#2-masuk-kedalam-virtual-environment)
    - [3. Mengunduh Semua Library](#3-mengunduh-semua-library)
    - [4. Atur SECRET\_KEY](#4-atur-secret_key)
      - [Generate key](#generate-key)
      - [Output](#output)
      - [Salin key ke .env](#salin-key-ke-env)
    - [5. Menjalankan Server](#5-menjalankan-server)
  - [Tailwind CSS (DEV)](#tailwind-css-dev)
    - [1. Atur beberapa hal](#1-atur-beberapa-hal)
      - [django\_app/settings.py](#django_appsettingspy)
      - [django\_app/urls.py](#django_appurlspy)
    - [2. Installing Tailwind](#2-installing-tailwind)
    - [3. Import ke html](#3-import-ke-html)
    - [4. Menjalankan compiler](#4-menjalankan-compiler)
  - [Tailwind CSS (PRODUCTION)](#tailwind-css-production)

## Instalasi

### 1. Menyiapkan Virtual Environment

```sh
py -m venv env 
```

[[Table of Content](#table-of-content)]

### 2. Masuk Kedalam Virtual Environment

Windows:
```sh
env/Scripts/activate
```

Unix:
```sh
source env/Scripts/activate
```
[[Table of Content](#table-of-content)]

### 3. Mengunduh Semua Library

```sh
py setup.py
```
[[Table of Content](#table-of-content)]

### 4. Atur SECRET_KEY

#### Generate key

```sh
py setup.py key
```

#### Output

```sh
Your key: '\8"0_V,GNhw2<"y4n{LO5eQ,8^n-jf:cPN+A~'}oQ/_Ld}@RII'
```

#### Salin key ke .env

Duplikasi file .env.example, ubah menjadi .env

```
# salin ke file .env
# dev | production
NODE_ENV=dev
SECRET_KEY='\8"0_V,GNhw2<"y4n{LO5eQ,8^n-jf:cPN+A~'}oQ/_Ld}@RII'
```

[[Table of Content](#table-of-content)]

### 5. Menjalankan Server

```sh
py setup.py -s
```

[[Table of Content](#table-of-content)]

## Tailwind CSS (DEV)

### 1. Atur beberapa hal

#### django_app/settings.py

```py
# django_app/settings.py

# tailwind setup
INTERNAL_IPS = ['127.0.0.1']
NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'
TAILWIND_APP_NAME = 'theme'

INSTALLED_APPS = [
  ...,
  'tailwind',
  'theme',
  'django_browser_reload',
]

MIDDLEWARE = [
  ...,
  "django_browser_reload.middleware.BrowserReloadMiddleware"
]
```

#### django_app/urls.py

```py
# django_app/urls.py
urlpatterns = [
  ...,
  path("__reload__/", include("django_browser_reload.urls")),
]
```

[[Table of Content](#table-of-content)]

### 2. Installing Tailwind

```sh
py setup.py -t --i
```

[[Table of Content](#table-of-content)]

### 3. Import ke html

```html
{% load static tailwind_tags %}

<!DOCTYPE html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="IE=7" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />

    {% tailwind_css %}
    <link rel="icon" href="{% static 'images/icon.png' %}" />

    <title>{{ title }}</title>
  </head>
  <body>
    <header>{% include 'partials/header.html' %}</header>
    {% block body %}{% endblock %}
    <footer>{% include 'partials/footer.html '%}</footer>
  </body>
  <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
</html>
```

[[Table of Content](#table-of-content)]

### 4. Menjalankan compiler

```sh
python setup.py -t --r
```

[[Table of Content](#table-of-content)]

## Tailwind CSS (PRODUCTION)