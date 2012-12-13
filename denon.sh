#!/bin/bash
echo -ne $1\\r| /usr/bin/nc -w1  192.168.1.130 23
