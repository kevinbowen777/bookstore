# Pull base image
From python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY .env Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# COPY . /code/
