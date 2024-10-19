
ARG PYTHON_BASE=3.9.13

FROM python:${PYTHON_BASE} as PYTHON_BASE

RUN pip install --upgrade pip pipenv

# Thanks Google Cloud Run! https://github.com/pypa/pipenv/issues/4174
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /usr/src

COPY . .
RUN chmod +x entrypoint.sh

RUN pipenv install --system --deploy

WORKDIR /usr/src/barbershop

# RUN pipenv run python manage.py migrate
# RUN pipenv run python manage.py collectstatic --noinput

EXPOSE 8000


ENTRYPOINT ["/usr/src/entrypoint.sh"]
