#!/usr/bin/env bash

export CONDUIT_SECRET='something-really-secret'
export FLASK_APP=./autoapp.py
export FLASK_DEBUG=0
export DATABASE_URL=postgresql://postgres:postgres@postgres/postgres

flask db init
#flask db migrate
flask db upgrade

#flask run --host=0.0.0.0 --with-threads
