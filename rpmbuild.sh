#!/bin/bash

IMAGE_NAME=centos6-python:2.7
BUILDER_DIR=$(pwd)
echo "Using docker image $IMAGE_NAME"
docker build --pull -t "$IMAGE_NAME" "$BUILDER_DIR"

docker build --pull -t $IMAGE_NAME $(pwd)

docker run \
    --net=host \
    -v "$(pwd)/rpmbuild:/rpmbuild:rw" \
    -t "$IMAGE_NAME" /build.sh
container=$(docker ps -l -q)
artifact_dir="artifacts/$IMAGE_NAME"
mkdir -p "$artifact_dir"
docker cp $container:/rpmbuild/RPMS "$artifact_dir"
