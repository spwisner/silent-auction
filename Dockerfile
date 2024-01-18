# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory in the container
WORKDIR /app

## copy requirements.txt
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]