FROM python:3.12.1-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["restaurant.asgi.handler"]
