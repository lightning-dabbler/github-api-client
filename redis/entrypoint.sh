#!/usr/bin/env bash
echo "Replacing _REDIS_PORT var with '$_REDIS_PORT' ..."
envsubst '$_REDIS_PORT:$_REDIS_PORT' < /source-dir/template.conf > /source-dir/redis.conf
redis-server /source-dir/redis.conf