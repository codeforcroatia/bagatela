FROM google/python

RUN apt-get install -y python-scrapy
WORKDIR /app
