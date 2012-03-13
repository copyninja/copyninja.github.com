#!/bin/sh

TAG=tag/
SITE=_site/

if [ -d ${TAG} ]; then
    echo "Deleting ${TAG} directory..."
    rm -rf ${TAG}
fi

echo "Regenerating Site..."
jekyll

echo "Copying ${TAG} ..."
cp -a ${SITE}/${TAG} .

# echo "Commiting Changes..."
# git commit ${TAG} -m "Latest TAG build"