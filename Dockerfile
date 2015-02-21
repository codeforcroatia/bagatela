FROM google/python

RUN apt-get install -y \
    build-essential \
    libffi-dev \
    openssl \
    python-lxml

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt
