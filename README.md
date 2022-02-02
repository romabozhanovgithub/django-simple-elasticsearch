# E-commerce

## Description
Simple work REST api with Elasticsearch

## Setup
### Backend
```
pip install -r requirements.txt
python manage.py makemagrations
python manage.py migrate
python manage.py populate_db
python manage.py runserver
```
And you will need to install elasticsearch and start

## Technologi Stack
- Django
- Django Rest Framework
- Elasticsearch
