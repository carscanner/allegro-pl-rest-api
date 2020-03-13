# Python SDK for Allegro.pl REST API

[![Build Status](https://travis-ci.com/mattesilver/allegro-pl-rest-api.svg)](https://travis-ci.com/mattesilver/allegro-pl-rest-api)
![PyPI](https://img.shields.io/pypi/v/allegro-pl-rest-api)

Built from OpenAPI definition at [Allegro API Monitor](/mattesilver/allegro-swagger)

See also:
- [Allegro API](https://github.com/allegro/allegro-api) official bug tracker and
- [allegro-pl](https://github.com/mattesilver/allegro-pl) python SDK for both REST and SOAP APIs

## Build process

### Prerequirements

[Java](https://www.java.com/) (To run OpenAPIGenerator)

[OpenAPIGenerator](https://github.com/OpenAPITools/openapi-generator)

[Python 3](https://www.python.org)

setuptools & wheel to build dist files

```shell script
pip3 install setuptools wheel
```


### Download Allegro OpenAPI definition

From [Allergo](https://developer.allegro.pl/swagger.yaml) or from my [Github repository](https://github.com/mattesilver/allegro-swagger)

### Generate client code

```shell script
openapi-generator generate -c openapi-generator-config.json -g python -i allegro.yaml -o generated
```

### build dist

In generated:
```shell script
python3 setup.py sdist bdist_wheel
```

### Upload to pypi

In generated:
```shell script
twine upload -r pypi -u $PYPI_USERNAME -p $PYPI_PASSWD --non-interactive dist/*
```
