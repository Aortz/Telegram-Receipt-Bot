# Use an official Python runtime as the base image
FROM python:3.11-slim

ENV PYTHONUNBUFFERED True

# Set the working directory in the container
WORKDIR /app
COPY *.txt .
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt
COPY . ./

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
# # Copy the current directory contents into the container at /app
# COPY . /app

# # # Install any needed dependencies specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 5000 available to the world outside this container
# EXPOSE 5000

# # Define environment variable
# # ENV TELEGRAM_BOT_TOKEN YOUR_BOT_TOKEN
# # RUN set -a && . ./.env && set +a

# # # Run main.py when the container launches
# # CMD ["python", "main.py"]
# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
