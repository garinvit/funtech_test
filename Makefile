down:
	docker-compose down

up:
	docker-compose up -d

build:
	docker-compose build

stop:
	docker-compose stop

start:
	docker-compose start

restart:
	docker-compose restart

psql:
	docker-compose exec postgres psql -U $(POSTGRES_USER) $(POSTGRES_DATABASE)

shell:
	docker-compose exec web python3 manage.py shell

logs:
	docker-compose logs --tail 100

ps:
	docker-compose ps

createsuperuser:
	docker-compose exec web python3 manage.py createsuperuser

makemigrations:
	docker-compose exec web python3 manage.py makemigrations

migrate:
	docker-compose exec web python3 manage.py migrate
