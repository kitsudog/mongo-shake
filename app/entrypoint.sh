#!/bin/bash
function fail
{
    echo $1
    exit 1
}
./check.py || fail "exit"
cat collector.conf.cur|grep '^#' -Ev|awk 'length($0)'|awk '{printf("%03s: %s\n",NR,$0)}'
diff -buB --ignore-all-space collector.conf.cur collector.conf|grep '^-'
nohup ./collector.linux -conf=collector.conf.cur &
# curl localhost:9101/progress -s|jq '.collection_metric[]' -r|awk -F'[()/]' '{sum+=$2;total+=$3}END{print sum*100/total}'
./progress.py
