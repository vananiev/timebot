#!/bin/bash

# Then buils throw proxy configure maven to use it and also uncomment
# JAVA_OPTS=-Dhttp.proxyHost=Host -Dhttp.proxyPort=8080

rm -f target/*.jar
mvn package || exit 1
exit 0
