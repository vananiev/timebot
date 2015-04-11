#!/bin/bash -x

dir=$(readlink -f $(dirname $0))
cd $dir

rm -f SOURCES/top/usr/lib/timebot/*.jar
cp ../target/*.jar SOURCES/top/usr/lib/timebot/timebot.jar
pushd SOURCES/top
tar -czf ../timebot.tar.gz .
popd
rpmbuild --define "_topdir $dir" -bb SPECS/timebot.spec || exit 1
exit 0
