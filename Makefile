build:
	docker build -t nababi_kitchen_image .

run:
	docker run --name nababi_kitchen_container -itd -p 3333:8000 nababi_kitchen_image python manage.py runserver 0.0.0.0:3333

stop:
	docker stop nababi_kitchen_container

r:
	python manage.py runserver

uvicorn:
	uvicorn restaurant.asgi:application --port 8000 --reload

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
	python backend/manage.py collectstatic

ecrtag:
	docker tag nababi_kitchen_image:latest 705538025739.dkr.ecr.eu-west-2.amazonaws.com/nababikitchen:latest

ecrpush:
	docker push 705538025739.dkr.ecr.eu-west-2.amazonaws.com/nababikitchen:latest

ecrbuild: build ecrtag ecrpush
