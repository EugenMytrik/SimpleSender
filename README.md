# SimpleSender
Попередньо створивши базу даних, запустіть контейнер брокера RabbitMQ у Docker
docker run -d -p 5672:5672 rabbitmq
Запустіть воркер Celery
celery -A djangoProject worker -l INFO
Якщо користуєтесь ОС Windows, можете спробувати ще
celery -A djangoProject worker -l INFO --pool=solo
Та сервер
python manage.py runserver
