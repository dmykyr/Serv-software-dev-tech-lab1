FROM python:3.13.0-bookworm

WORKDIR /myapp


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . /myapp


CMD flask --app ./__init__.py  run -h 0.0.0.0 -p $PORT
