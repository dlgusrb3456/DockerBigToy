#!/bin/bash
docker stack deploy -c $1 $2 # $1 : yml 파일, $2 : stack/service name
