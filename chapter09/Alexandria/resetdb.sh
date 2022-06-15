#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
rm -rf catalog/migrations people/migrations review/migrations

rm ../uploads/Alexandria/*
cp ../../data/Conan_Doyle.jpg ../uploads/Alexandria/1_Conan_Doyle.jpg
cp ../../data/Hemingway.jpg ../uploads/Alexandria/Hemingway.jpg

# django db and test data process
python manage.py makemigrations people catalog review
python manage.py migrate

python manage.py loaddata ../../data/ch08.json
