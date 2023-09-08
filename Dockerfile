# Use an official Python runtime as a parent image
FROM python:3.10-alpine3.17

#Install bin
RUN apk add  iptables
RUN apk add curl
RUN apk add vim
# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run your Python script when the container launches
CMD ["python", "fakeport.py"]
