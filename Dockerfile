FROM python:3.9-slim-bullseye

RUN mkdir -p /app
WORKDIR /app

RUN apt update
RUN apt install pandoc -y
RUN apt install nginx -y
RUN apt install git -y

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY source source
COPY .git .git
COPY nginx_docker.conf /etc/nginx/nginx.conf

RUN sphinx-build -b html source _build
CMD ["nginx", "-g", "daemon off;"]
