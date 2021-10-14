FROM alpine:latest

RUN apk update \
  && apk add python3 \
  && apk add py3-pip \
  && mkdir /usr/local/api_django

COPY api_with_restrictions  /usr/local/api_django

WORKDIR /usr/local/api_django

RUN pip install -r requirements.txt \
  && python3 manage.py migrate \
  && python3 manage.py makemigrations advertisements \
  && python3 manage.py migrate

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
