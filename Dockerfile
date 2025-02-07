# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx && \
    rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Nginx configuration
COPY ./nginx/conf.d/default.conf /etc/nginx/conf.d/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 80 for Nginx
EXPOSE 80

# Start Nginx and Gunicorn
CMD service nginx start && \
    gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
