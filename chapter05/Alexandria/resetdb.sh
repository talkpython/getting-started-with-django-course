#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
rm -rf catalog/migrations
python manage.py makemigrations catalog
python manage.py migrate
python manage.py loaddata ../../data/ch05.json
