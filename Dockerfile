FROM python:3.9-bookworm

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY source .

# RUN add-apt-repository ppa:nginx/stable
RUN apt update
RUN apt install pandoc -y
RUN apt install nginx -y

COPY nginx_docker.conf /etc/nginx/nginx.conf

RUN sphinx-build -b html source build
CMD ["nginx", "-g", "daemon off;"]
