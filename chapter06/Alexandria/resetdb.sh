#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
rm -rf catalog/migrations people/migrations
python manage.py makemigrations people catalog
python manage.py migrate
python manage.py loaddata ../../data/ch06.json
