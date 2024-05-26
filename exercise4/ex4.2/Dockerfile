FROM python:3.10.3-slim

copy . /myapp
WORKDIR /myapp

RUN apt-get update
RUN apt-get install -y curl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
RUN install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
RUN pip install -r req.txt

CMD python controller.py