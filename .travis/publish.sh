#!/usr/bin/env bash

version=$(grep 'VERSION =' setup.py|cut -d' ' -f3| tr -d '"')

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*${version}*
