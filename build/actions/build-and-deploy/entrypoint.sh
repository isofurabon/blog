#!/bin/sh -eu
ls -al
echo "retrive & generate posts"
python3 build/actions/build-and-deploy/retrive_and_generate_posts.py
ls -al