# Use an official TensorFlow runtime as a parent image
FROM python:3.9

RUN apt-get update && \
    apt-get install -y git

# Set the working directory in the container
WORKDIR /app/Proyecto-Cloud

# Clone the GitHub repository containing the machine learning model
RUN git clone https://github.com/Oteranga/Proyecto-Cloud.git

# Install any additional dependencies required by your project
RUN python3 -m pip install --upgrade pip
#RUN pip install -r /app/Proyecto-Cloud/requirements.txt

# Expose the port your application will run on
EXPOSE 5000

# Define environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Command to run on container start
CMD ["flask", "run"]
