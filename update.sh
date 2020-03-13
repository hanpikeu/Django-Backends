#!/bin/bash
git reset --hard
git fetch
git pull
source .venv/bin/activate
python3 manage.py migrate