#!/bin/bash

./build-standalone.sh && ./rpmbuild/mkrpm.sh && echo "rpm builded in rpmbuild/RPMS/"
