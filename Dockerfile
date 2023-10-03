# Start from a Python 3.9 base image
FROM python:3.9

# Set the working directory in the image
WORKDIR /app

# Copy the requirements.txt file into the image
COPY requirements.txt .

# Install the dependencies using pip
RUN pip install -r requirements.txt

# Copy the project files into the image
COPY . .

# Set the Django settings module and the Python unbuffered output variable
ENV DJANGO_SETTINGS_MODULE=image_uploader.docker
ENV PYTHONUNBUFFERED=1

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]