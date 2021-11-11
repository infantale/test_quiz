# test_quiz

Доступные учетные записи

| Тип пользователя | Логин   | Пароль      |
| ---------------- | ------- | ------------|
| Админ            | admin   | password123 |


# Установка

Для запуска на ПК должны быть установлены:
[Python 3.7](https://www.python.org/downloads/);
[Git](https://git-scm.com/);

Склонируйте репозиторий

```sh
$ git clone https://github.com/infantale/test_quiz.git
```

### 1) Настройка Django

В корне проекта создайте виртуальное окружение и активируйте его

```sh
$ cd .\quiz\
$ python -m venv “venv”
$ .\venv\Scripts\activate (для Linux: source ./venv/bin/activate)
```

#### Все последующие действия производить внутри виртуального окружения

Установите все необходимые зависимости для работы Django

```sh
$ pip install -r requirements.txt
```

Запустите проект

```sh
$ python manage.py runserver
```
