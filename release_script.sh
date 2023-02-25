#!/bin/sh
version=$(git log --format=%B -n 1)
release_type=$(echo $version | awk -F" " '{print $1}')
current_version=$(poetry version -s)
new_version=$(python cicd_scripts/get_version.py version $current_version $release_type)
echo ${new_version}
commit_message=$(python cicd_scripts/get_version.py commit_message $new_version $release_type)
echo $commit_message
poetry version $new_version
git add .
git commit -m "${commit_message}"
git tag $(poetry version -s) HEAD
git push
git push --tags 