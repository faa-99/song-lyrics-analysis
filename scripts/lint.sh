#!/usr/bin/env bash

set -e
set -x

mypy app.py utils.py viz.py
flake8 app.py utils.py viz.py
black app.py utils.py viz.py
isort app.py utils.py viz.py