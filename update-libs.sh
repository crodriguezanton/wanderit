#!/bin/bash

cd ../../django-skyscanner
python setup.py sdist
pip install /Users/crodriguezanton/Documents/Beat.bcn/Development/django-skyscanner/dist/django-skyscanner-$1.tar.gz --upgrade
cd ../wanderit/wanderit
