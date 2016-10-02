#!/bin/sh

docker run --rm -ti -p 9000:443 -p 8000:80 -p 2022:22 bernws2016/trinity $*

