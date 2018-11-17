# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Install update packages list
RUN apt-get update 

# Install linux packages
RUN apt-get install -y gcc

# Install any needed packages 
RUN pip install responder 

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Define environment variable
ENV PORT '5000'

# Make port 80 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD python3 app.py