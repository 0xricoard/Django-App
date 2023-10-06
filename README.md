# Estimasi Harga Mobil Bekas

## Table of Content
- [Estimasi Harga Mobil Bekas](#estimasi-harga-mobil-bekas)
  - [Table of Content](#table-of-content)
  - [Instalasi](#instalasi)
    - [1. Menyiapkan Virtual Environment](#1-menyiapkan-virtual-environment)
    - [2. Masuk Kedalam Virtual Environment](#2-masuk-kedalam-virtual-environment)
    - [3. Mengunduh Semua Library](#3-mengunduh-semua-library)
    - [4. Menjalankan Server](#4-menjalankan-server)
  - [Install Tailwind CSS](#install-tailwind-css)
    - [1. Atur lokasi NPM](#1-atur-lokasi-npm)
    - [2. Import ke html](#2-import-ke-html)
    - [3. Menjalankan compiler](#3-menjalankan-compiler)
    - [4. Production](#4-production)

## Instalasi

### 1. Menyiapkan Virtual Environment

```sh
py -m venv env 
```

### 2. Masuk Kedalam Virtual Environment

Windows:
```sh
env/Scripts/activate
```

Unix:
```sh
source env/Scripts/activate
```

### 3. Mengunduh Semua Library

```sh
py setup.py
```

### 4. Menjalankan Server

```sh
py manage.py runserver
```

## Install Tailwind CSS

### 1. Atur lokasi NPM
```py
# django_app/settings.py

NPM_BIN_PATH = r'C:\Program Files\nodejs\npm.cmd'
```

### 2. Import ke html
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

### 3. Menjalankan compiler
```sh
python manage.py tailwind start
```

### 4. Production