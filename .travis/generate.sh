#!/usr/bin/env bash
SWAGGER_FILE=$(dirname "$0")/swagger.yaml
curl -o $SWAGGER_FILE https://developer.allegro.pl/swagger.yaml

CONFIG_FILE=$(dirname "$0")/swagger-config.json
TARGET_DIR=$(dirname "$0")/..
openapi-generator generate -c $CONFIG_FILE -g python -i $SWAGGER_FILE -o $TARGET_DIR
