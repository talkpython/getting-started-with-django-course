#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
#rm -rf ../outside/Vye/account_uploads
#rm -rf ../outside/Vye/thumbnails
rm -rf catalog/migrations

# django db and test data process
python manage.py makemigrations catalog
python manage.py migrate
