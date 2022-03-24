#!/bin/bash

today=$(date "+%y.%m.%d")

git fetch --all
git add *
git commit -m "${today}"
git push origin main