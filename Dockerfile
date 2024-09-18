FROM python:3.12.1-slim

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Step 3: Set the working directory
WORKDIR /app

# Step 4: Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Step 5: Copy project files to container
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Step 6: Expose the port Django will run on
EXPOSE 8000

# Step 7: Run migrations and start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
