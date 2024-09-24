FROM python:3.12.1-slim
WORKDIR /app
COPY backend /app
RUN pip install --upgrade pip && pip install -r layer/requirements.txt
RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
