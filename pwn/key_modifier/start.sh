#!/bin/sh

while :
do
	exec socat TCP-LISTEN:55556,reuseaddr,fork,forever,keepalive EXEC:'/home/ctf/challenge'
done
