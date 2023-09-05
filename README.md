# WHERE_TO_GO

<img width="446" alt="Screenshot_25" src="https://github.com/RomanRVV/where_to_go/assets/129319859/72df33e5-e1f5-406a-a60f-f01ef561cbcb">

Сайт созданный для добавления и отображения интересных мест в городе Москве.
Позволяет удобно добавлять и редактировать информацию о местах, через административную панель.

[Ссылка на готовый сайт](https://romarv.pythonanywhere.com/)

[Ссылка на административную панель](https://romarv.pythonanywhere.com/admin/)


### Как запустить

Для запуска сайта вам понадобится Python третьей версии.

Скачайте код с GitHub. Затем установите зависимости

```sh
pip install -r requirements.txt
```

Создайте базу данных:

```sh
python3 manage.py makemigrations
python3 manage.py migrate
```
Создайте суперпользователя
```sh
python3 manage.py createsuperuser
```

Запустите разработческий сервер

```sh
python3 manage.py runserver
```

Для входа в админ-панель откройте ссылку /admin (например http://127.0.0.1:8000/admin) и введите логин и пароль суперпользователя


### Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 2 переменные:
- `DEBUG` — дебаг-режим. Поставьте True, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `ALLOWED_HOSTS` — см [документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts).


### Загрзука данных на сайт:

Данные на сайт можно добавлять двумя способами:


1 Через административную панель 

2 Загружая данный из json файла с помощью команды([пример файла](https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%AF%D0%BF%D0%BE%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D1%81%D0%B0%D0%B4.json)):

```sh
python3 manage.py load_place
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
