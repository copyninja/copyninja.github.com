#!/bin/sh
set -x

if [ $# -eq 0 ]; then
    echo "Usage: $0 draft-file-name remove-draft"
    exit 2
fi

DRAFT_DIRECTORY=$(pwd)/_drafts
POST_DIRECTORY=$(pwd)/_posts
POST_NAME=$(date +'%F')"-$1"

echo "Publishing $1.."
cp -a ${DRAFT_DIRECTORY}/$1 ${POST_DIRECTORY}/${POST_NAME}
jekyll

if [ $2 -eq 1 ]; then
    rm ${DRAFT_DIRECTORY}/$1
fi

