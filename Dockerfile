FROM python:3.11.3-slim-buster

LABEL maintainer="MCSDevTeam"

RUN pip install pipenv

ENV PROJECT_DIR /app

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/
RUN pip install pipenv
RUN pipenv install --system --deploy --ignore-pipfile
RUN pipenv install gunicorn

COPY . ${PROJECT_DIR}/

EXPOSE 8080

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8080", "app:app"]