#!/usr/bin/env bash

CONFIG_FILE=openapi-generator-config.json
SWAGGER_FILE=allegro.yaml

pull_api(){
  git clone --depth 1 https://github.com/mattesilver/allegro-swagger.git allegro-openapi
}

current_version(){
  return $(grep 'VERSION ='generated/setup.py|cut -d' ' -f3| tr -d '"')
}

new_version(){
  cat allegro-openapi/VERSION
}

is_changed(){
  if [ -d generated ]; then
    if [ current_version = $VERSION ]; then
      echo no change
      return 0
    else
      return 1
    fi
  else
    return 1
  fi
}

mk_generator_config(){
  echo > $CONFIG_FILE \
"{
  \"packageName\": \"allegro_api\",
  \"projectName\": \"allegro-pl-rest-api\",
  \"hideGenerationTimestamp\": \"false\",
  \"packageVersion\": \"$VERSION\"
}"
  git add $CONFIG_FILE
}

generate(){
  ~/openapi-generator-cli.sh generate -c $CONFIG_FILE -g python -i $SWAGGER_FILE -o generated
  git add generated
}


pull_api
VERSION=$(new_version)
if [ is_changed ]; then
  git rm -r generated

  export CHANGED=1
  sed  "s/version\: 'latest'/version\: '$VERSION'/" allegro-openapi/allegro-openapi.yaml > $SWAGGER_FILE
  git add $SWAGGER_FILE
  mk_generator_config
  generate
fi

rm -rf allegro-openapi
export VERSION
