FROM python:3.12.1-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000
CMD ["uvicorn", "restaurant.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
