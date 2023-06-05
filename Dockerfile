FROM python:3.8

LABEL maintainer="Olaide Alaka"

WORKDIR /app

# Copy the app code
COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# upgrade pip
RUN pip install --upgrade pip

# Install dependencies
RUN pip install -r requirements.txt

# migrate database
RUN python manage.py migrate

# collect static files
RUN python manage.py collectstatic

# Expose port
EXPOSE 8000

# command to Run the Django development server on container start 
CMD ["python", "manage.py", "runserver"]
