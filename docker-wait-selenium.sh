#!/bin/sh
set -e 
wait-for-it selenium_chrome:4444
exec "$@"