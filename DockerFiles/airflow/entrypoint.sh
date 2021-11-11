#!/usr/bin/env bash

# Initiliase the metastore
airflow db init

# Run the scheduler in background
airflow users create --username Admin \
    --firstname mateusz \
    --lastname borsuk \
    --role Admin \
    --password admin \
    --email mtszborsuk212@gmai.com

airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver