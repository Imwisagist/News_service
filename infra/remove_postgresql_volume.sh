#!/bin/bash
# Остановка и удаление контейнеров
docker-compose down
# Удаление волюма Постгрес
docker-compose volume rm infra_postgres_data
