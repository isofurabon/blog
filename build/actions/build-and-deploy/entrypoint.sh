#!/bin/sh -l
ls -al

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"