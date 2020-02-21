#!/usr/bin/env bash

pip3 install setuptools wheel
pushd generated
python3 setup.py sdist bdist_wheel
popd
