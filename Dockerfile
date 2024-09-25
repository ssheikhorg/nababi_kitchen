FROM python:3.12.1-slim
WORKDIR /app
COPY backend /app
RUN pip install --upgrade pip && pip install -r layer/requirements.txt
RUN python manage.py collectstatic --noinput
CMD ["python", "manage.py", "runserver"]
