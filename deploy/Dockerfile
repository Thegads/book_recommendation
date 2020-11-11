FROM scrapinghub/scrapinghub-stack-scrapy:1.3
from python:3.7-slim
COPY . /app
WORKDIR /app

RUN apt-get update                             \
 && apt-get install -y --no-install-recommends \
    ca-certificates curl firefox-esr           \
 && rm -fr /var/lib/apt/lists/*                \
 && curl -L https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz | tar xz -C /usr/local/bin \
 && apt-get purge -y ca-certificates curl


RUN pip install --no-cache-dir -r requirements.txt
RUN python db_starter.py

#CMD gunicorn --bind 0.0.0.0:5000 wsgi
CMD gunicorn --bind 0.0.0.0:$PORT wsgi