#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
rm -rf catalog/migrations people/migrations review/migrations
python manage.py makemigrations people catalog review
python manage.py migrate
python manage.py loaddata ../../data/ch07.json
