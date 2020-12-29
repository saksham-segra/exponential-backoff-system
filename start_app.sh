#!/bin/bash
python /src/agri_app/manage.py migrate
python /src/agri/manage.py runserver 0.0.0.0:8080