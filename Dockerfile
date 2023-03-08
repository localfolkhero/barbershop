#
ARG PYTHON_BASE=3.9

FROM python:${PYTHON_BASE} as PYTHON_BASE

RUN pip install --upgrade pip pipenv

# Thanks Google Cloud Run! https://github.com/pypa/pipenv/issues/4174
ENV PIPENV_VENV_IN_PROJECT 1

WORKDIR /usr/src

COPY ./Pipfile .
COPY ./Pipfile.lock .

COPY . .

RUN pipenv install 

WORKDIR /usr/src/barbershop

RUN pipenv run python manage.py collectstatic --noinput

EXPOSE 8000

ENTRYPOINT [ "pipenv" ]
CMD ["run", "gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "barbershop.wsgi"]