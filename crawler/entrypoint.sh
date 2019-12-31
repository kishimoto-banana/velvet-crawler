#!/bin/bash
cd /crawler/database
orator migrate -f
#cd /crawler/hatena_crawler

exec "$@"
