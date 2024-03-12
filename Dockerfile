# syntax=docker/dockerfile:1
FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
COPY /nginx.conf /etc/nginx/nginx.conf
RUN pip install -r requirements.txt
COPY . /code/
RUN pip install --upgrade pip
CMD ["nginx", "-g", "daemon off;"]
EXPOSE 80
