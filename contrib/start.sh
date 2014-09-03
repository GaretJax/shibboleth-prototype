#!/bin/sh
/sbin/service shibd start
/usr/sbin/httpd -DFOREGROUND
