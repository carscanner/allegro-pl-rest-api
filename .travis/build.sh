#!/usr/bin/env bash

pushd generated
pip3 install setuptools wheel
python3 setup.py sdist bdist_wheel
popd
