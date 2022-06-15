#!/bin/bash

find . -name "*.pyc" -exec rm {} \;
rm db.sqlite3
python manage.py migrate
