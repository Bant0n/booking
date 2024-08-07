# Бронирование отелей

Это репозиторий к курсу о бэкенд разработке на Python с упором на изучение FastAPI и работы с SQLAlchemy, Celery, Redis, Docker, а также многими другими библиотеками и технологиями.

## Запуск приложения

Для запуска FastAPI используется веб-сервер uvicorn. Команда для запуска выглядит так:

``` bash
uvicorn main:app --reload
```

Либо же:

``` bash
python main.py
```

Ее необходимо запускать в командной строке.

### Celery & Flower

Для запуска Celery используется команда

``` bash
celery --app=app.tasks.celery:celery worker -l INFO -P solo
```

Обратите внимание, что `-P solo` используется только на Windows, так как у Celery есть проблемы с работой на Windows.
Для запуска Flower используется команда

```bash
celery --app=app.tasks.celery:celery flower
```

### Dockerfile

Для запуска веб-сервера (FastAPI) внутри контейнера необходимо запустить Dockerfile и иметь уже запущенный экземпляр PostgreSQL на компьютере.
Код для запуска Dockerfile:

```bash
docker build .
```

Команда также запускается из корневой директории, в которой лежит файл Dockerfile.

### Docker compose

Для запуска всех сервисов (БД, Redis, веб-сервер (FastAPI), Celery) необходимо использовать файл docker-compose.yml и команды

```bash
docker compose build
docker compose up
```

Причем `build` команду нужно запускать, только если вы меняли что-то внутри Dockerfile, то есть меняли логику составления образа.

## Telegram

<https://t.me/B4nton>
