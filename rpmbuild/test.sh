#!/bin/bash

# $1 - testing timebot.jar

cd $(dirname $0)

java -jar $1 &>/tmp/timebot.log &
pid="$!"
cnt=0
while true; do
	sleep 2
	netstat -ltn | grep 8080 &>/dev/null && break
	cnt=$((cnt+1))
	if [ "$cnt" -ge 10 ]; then
		kill $pid || kill -9 $pid
		exit 1
	fi
done
unset http_proxy
exitcode=1
wget -O - http://localhost:8080/ | grep Hello &>/dev/null && { grep --color "\[ERROR\]" /tmp/timebot.log &>/dev/null  || exitcode=0; }
kill $pid || kill -9 $pid
exit $exitcode
