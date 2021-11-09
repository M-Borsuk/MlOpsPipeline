#!/usr/bin/env bash

if [ -f .env ]
then
  export $(cat .env | sed 's/#.*//g' | xargs)
fi

# Initiliase the metastore
airflow db init

# Run the scheduler in background
# airflow users create --username ${AIRFLOW_USER} \
#     --firstname ${AIRFLOW_FIRST_NAME} \
#     --lastname ${AIRFLOW_LAST_NAME} \
#     --role Admin \
#     --password ${AIRFLOW_PASSWORD} \
#     --email ${AIRFLOW_EMAIL}

airflow scheduler &> /dev/null &

# Run the web sever in foreground (for docker logs)
exec airflow webserver