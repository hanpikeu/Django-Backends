#!/bin/bash
pid=`cat django.pid`
kill -9 $pid
pid=$((pid+1))
kill -9 $pid