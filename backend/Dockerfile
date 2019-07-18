FROM python:3

RUN mkdir /usr/src/wordsum
WORKDIR /usr/src/wordsum
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN mkdir /usr/src/wordsum/production
COPY app production/app

EXPOSE 8000 8000

CMD ["python", "production/app/main.py"]
