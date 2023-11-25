FROM python:3.9

WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
