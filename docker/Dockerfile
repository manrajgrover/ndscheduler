FROM python:3.6-alpine

MAINTAINER Manraj Singh <manrajsinghgrover@gmail.com>

ADD . /root
WORKDIR /root

RUN pip install virtualenv

RUN virtualenv /venv && \
    source /venv/bin/activate && \
    pip install -r ./scheduler/requirements.txt && \
    pip install .

RUN chmod 755 ./scheduler/docker.sh

CMD ["./scheduler/docker.sh"]
