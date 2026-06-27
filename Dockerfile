ARG PYTHON_BASE=3.9.13

FROM python:${PYTHON_BASE}

RUN pip install --upgrade pip pipenv

WORKDIR /usr/src

COPY Pipfile Pipfile.lock ./

RUN pipenv install --system --deploy

COPY . .

WORKDIR /usr/src/barbershop

EXPOSE 8000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/usr/src/entrypoint.sh"]
