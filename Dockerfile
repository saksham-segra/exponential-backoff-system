FROM python:3.8.2-alpine3.11

RUN apk update \
 && apk add postgresql-dev gcc python3-dev build-base \
 && dos2unix

RUN apk --no-cache add libpq libressl-dev libffi-dev musl-dev

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY start_app.sh .
RUN chmod +x start_app.sh
RUN dos2unix start_app.sh

WORKDIR /src

RUN pip install pip-tools
COPY requirements.in .

RUN pip-compile --generate-hashes --output-file=/src/requirements.txt requirements.in
RUN pip install -r requirements.txt

RUN pip uninstall -y pip-tools

WORKDIR /src/agri
COPY ./agri .

RUN apk del libpq libressl-dev libffi-dev musl-dev

RUN adduser -D in_user
USER in_user

EXPOSE 8080


CMD ["/bin/sh", "/start_app.sh"]