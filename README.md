## Bookstore 

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/bookstore.svg)](https://github.com/kevinbowen777/bookstore/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

- A basic bookstore application built using the Django 4.1 web framework

---
## Features
 - Application
     - Add book reviews
     - Upload book covers
     - Basic search capability
     - User registration with email verification & social(GitHub) login
     - Bootstrap4 & crispy-forms decorations
     - Customizable user profile pages with bio, profile pic, & country flags
 - Dev/testing
     - basic module testing templates
     - Coverage reports
     - Debug-toolbar available
     - Examples of using Factories & pytest fixtures in account app testing
     - `shell_plus` with IPython via `django-extensions` package
     - Nox testing sessions for latest Python 3.9, 3.10, and 3.11
         - black
         - Sphinx documentaion generations
         - linting
             - flake8
             - flake8-bugbear
             - flake8-docstrings
             - flake8-import-order
         - safety(python package vulnerability testing)
         - pytest sessions with coverage
 - User registration with email verification & social(GitHub) login
 - Bootstrap4 & crispy-forms decorations
 - Customizable user profiles with bio, profile picture & country flags
 - Nox testing sessions (black, linting, pytest, coverage, Sphinx doc generation)
 - uses django-debug-toolbar in DEBUG mode

### Installation
 - `git clone https://github.com/kevinbowen777/bookstore.git`
 - `cd bookstore`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

### Live Demo on Heroku:
 - https://kbowen-django-bookstore.herokuapp.com/

### Docker Container Image:

 - TBD
---
## Screenshots

### Home
![Home](https://github.com/kevinbowen777/bookstore/blob/master/images/bookstore_home.png)

### Search Results
![Search Results](https://github.com/kevinbowen777/bookstore/blob/master/images/bookstore_search-results.png)

### Book detail with reviews
![Book detail](https://github.com/kevinbowen777/bookstore/blob/master/images/bookstore_detail-review.png)

### Book detail with django-debug-toolbar
![Detail debug-toolbar](https://github.com/kevinbowen777/bookstore/blob/master/images/bookstore_booklist_debug-toolbar.png)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/bookstore/issues)
      to view currently open bug reports or open a new issue.
