#!/bin/sh

docker run --rm -ti -v `pwd`:/home/rstudio -p 10000:8787 bernws2016/scell $*

