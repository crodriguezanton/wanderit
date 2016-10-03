#!/bin/bash

cd ../../django-skyscanner
python setup.py sdist
cd ../wanderit/wanderit
pip install ../../django-skyscanner --upgrade
