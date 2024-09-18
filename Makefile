db-create:
	docker run --name nababi-db \
		-e POSTGRES_USER=admin \
		-e POSTGRES_PASSWORD=N@babiKitchen \
		-e POSTGRES_DB=nababikitchendb \
		-p 5432:5432 \
		-v db_data:/var/lib/postgresql/data \
		-d postgres

db:
	docker start nababi-db

stop:
	docker stop nababi-db

r:
	python manage.py runserver

n:
	python manage.py makemigrations

t:
	python manage.py migrate

su:
	python manage.py createsuperuser

i:
	pip install -U -r requirements.txt

collect:
	python manage.py collectstatic

deploy:
	zappa deploy production

update:
	zappa update production
