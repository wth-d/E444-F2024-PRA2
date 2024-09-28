# v1 (official)
# this is an official Python runtime, used as the parent image
# FROM python:3.12.6-slim

# WORKDIR /app

# COPY requirements.txt requirements.txt

# RUN apt-get update
# RUN apt-get -y install gcc
# RUN pip3 install -r requirements.txt
# COPY . .
# ENV FLASK_APP=hello.py
# # expose all IP addresses with 0.0.0.0??
# CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]




# v2
# works if 0.0.0.0 is set in hello.py when calling app.run()

FROM python:3.12.6-slim

# add the current directory to the container as /app
ADD . /app

# set the working directory in the container to /app
WORKDIR /app


# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Flask app to run on
EXPOSE 5000

# RUN export FLASK_APP=hello.py
# RUN export FLASK_DEBUG=1

# execute the Flask app
CMD ["python", "hello.py"]
# CMD ["flask", "run"]



# v3 - doesn't work so well

# FROM ubuntu:latest
# RUN apt-get update -y
# RUN apt install -y python3-pip python3 build-essential
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["hello.py"]
