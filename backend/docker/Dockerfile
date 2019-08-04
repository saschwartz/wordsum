FROM python:3

RUN mkdir /usr/src/wordsum
WORKDIR /usr/src/wordsum
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir production
COPY app production/app

EXPOSE 8000 8000

CMD ["gunicorn", "--chdir", "/usr/src/wordsum/production/app", "--bind", "0.0.0.0:8000", "wsgi:app"]
