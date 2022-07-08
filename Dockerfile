FROM python:3.6-slim as base

RUN apt-get update
RUN apt-get -y install netcat

WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install gunicorn
RUN pip install -r requirements.txt
COPY . .

RUN adduser --disabled-password --gecos '' default
RUN chmod +x boot.sh
USER default

FROM base as run
EXPOSE 5005
ENV PYTHONPATH=.:api
CMD ["./boot.sh"]
