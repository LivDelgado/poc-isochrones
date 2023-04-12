#! /usr/bin/env bash
echo "Waiting for postgres connection"

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    sleep 0.1
done

echo "PostgreSQL started"

exec "$@"