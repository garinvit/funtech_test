# Установка

```bash
git clone git@github.com:garinvit/funtech_test.git

cd funtech_test
```

Переключаемся на ветку `main`

```bash
git checkout main

git push -u origin main
```

Копируем файл `.env.example` в файл `.env`

```bash
cp .env.example .env.dev
```

Редактируем файл '.env.dev', 
заполняем своими данными.
Особенно важно задать:
- SECRET_KEY

Запускаем проект
(миграции применятся сами)

```bash
make up
```

Создать суперпользователя

```bash
make createsuperuser
```

Создать миграции

```bash
make makemigrations
```

Применить миграции вручную

```bash
make migrate
```