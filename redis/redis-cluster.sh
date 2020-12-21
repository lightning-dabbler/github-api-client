#!/usr/bin/env bash

yes yes | redis-cli -p 6379 --cluster create 10.0.0.11:6380 \
10.0.0.12:6381 10.0.0.13:6382 10.0.0.14:6383 \
10.0.0.15:6384 10.0.0.16:6385 --cluster-replicas 1 --cluster-yes