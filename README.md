Доброго дня! В этом проекте можно управлять городами и их расположениям, всё в соответствии CRUD. Используемые технологии: Python, django, drf, postgresql, celery, redis.

Старт проекта:
1)Локально: Проект можно запустить локально, изменив в настройках bd DB_HOST на DB_HOST_LOCAL.

2)Docker: команда docker-compose up из директории где находится файл docker-compose.yml
Так же необходимо выполнить две доп. команды для работы и тестирования:
1. docker exec -it cdnvideo-web-1 python manage.py migrate
2. docker exec -it cdnvideo-web-1 python manage.py loaddata cities.json

Все маршруты по которым можно протестировать работу приложения указаны в map/urls.py
!!! Внимание !!! к указаным маршрутам в начале ещё добавляется api/

Пример запроса для двух ближайших городов - http://localhost:8000/api/cities/100.2323/50.9587/
