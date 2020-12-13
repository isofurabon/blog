#!/bin/sh -eux
echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"

python3 build/actions/build-and-deploy/retrive_and_generate_posts.py