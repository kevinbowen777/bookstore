## bookstore - A web application built with Docker and Django web framework

---
## Features
 - add book reviews
 - upload book covers
 - basic search capability
 - email verification for account registration & password/email change
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
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/kevinbowen777/bookstore/blob/master/LICENSE)
---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/bookstore/issues)
      to view currently open bug reports or open a new issue.
