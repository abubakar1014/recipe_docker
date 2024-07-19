# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgrade pip before installing all requirements
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
# ENV DJANGO_SETTINGS_MODULE=testing.settings

# Run the application with Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "testing.wsgi:application"]
