#!/usr/bin/env bash

set -e
set -x

black  app.py utils.py viz.py
isort  app.py utils.py viz.py