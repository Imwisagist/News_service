#!/bin/bash
# Остановка и удаление контейнеров
docker-compose down
# Пересборка и запуск контейнеров в фоновом режиме
docker-compose up -d --build
# Выполнение миграций базы данных
docker-compose exec backend poetry run python manage.py migrate
# Сбор статических файлов
docker-compose exec backend poetry run python manage.py collectstatic --no-input
