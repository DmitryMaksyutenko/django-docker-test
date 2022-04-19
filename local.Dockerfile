FROM python:3.10

ENV PYTHONFAULTHANDLER=1 \ 
	PYTHONHASHSEED=random \
	PYTHONPATH=${PYTHONPATH}:/django-test-app/__pypackages__/3.10/lib

RUN adduser admin

RUN pip install pdm 

RUN mkdir /django-test-app

COPY . /django-test-app

WORKDIR /django-test-app/config

RUN chown -R admin /django-test-app

USER admin

RUN pdm install
