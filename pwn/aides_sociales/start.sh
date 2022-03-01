#!/bin/sh

while :
do
	exec socat TCP-LISTEN:55555,reuseaddr,fork,forever,keepalive EXEC:'/home/ctf/challenge'
done

#/etc/init.d/xinetd start;
#sleep infinity;
