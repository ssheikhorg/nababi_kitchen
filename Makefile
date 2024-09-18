build:
	docker build -t nababi_kitchen_image .

run:
	docker run --name nababi_kitchen_container -itd -p 8000:8000 nababi_kitchen_image

stop:
	docker stop nababi_kitchen_container

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

i-dev:
	pip install -U -r requirements-dev.txt

collect:
	python manage.py collectstatic

deploy:
	zappa deploy production

update:
	zappa update production
