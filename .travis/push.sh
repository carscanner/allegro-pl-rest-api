#!/bin/bash

setup_git() {
  git config --global user.email "rafalkrupinski@users.noreply.github.com"
  git config --global user.name "Travis CI"
}

commit_changes() {
  git add generated
  git commit --message "New version: $VERSION"
}

upload_files() {
  git remote add my-origin https://${GH_TOKEN}@github.com/mattesilver/allegro-pl-rest-api > /dev/null 2>&1
  git push --set-upstream my-origin $TRAVIS_BRANCH
}

setup_git
commit_changes
upload_files
