#!/bin/bash

rm -f target/*.jar
mvn package || exit 1
exit 0
