FROM ubuntu:16.04

MAINTAINER Manraj Singh <manraj.singh@practo.com>

# Ubuntu requirements
RUN apt-get update && \
    apt-get install -y software-properties-common apt-transport-https

# Install R
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN add-apt-repository 'deb [arch=amd64,i386] https://cran.rstudio.com/bin/linux/ubuntu xenial/' -y && \
    apt-get update && \
    apt-get install -y r-base libcurl4-gnutls-dev libxml2-dev libssl-dev


# Install Python 3.6
RUN add-apt-repository ppa:deadsnakes/ppa -y && \
    apt-get update && \
    apt-get install -y python3.6 python3.6-dev

# Link Python to Python 3.6
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.6 1

# Install PIP
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

# Install virtualenv
RUN pip install virtualenv==15.2.0

ARG SCHEDULER_PATH=/root/ndscheduler

ADD . $SCHEDULER_PATH
WORKDIR $SCHEDULER_PATH

RUN virtualenv /venv && \
    . /venv/bin/activate && \
    pip install -r ./scheduler/requirements.txt && \
    pip install -e .

# CRON Specific dependencies

## R
RUN apt-get update && \
    apt-get install -y libpq-dev libmysqlclient-dev

# Clean up commands
RUN rm -rf /root/.cache/pip/* && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /usr/local/src/*

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN chmod 755 ./scripts/docker.sh

EXPOSE 8888

CMD ["/root/ndscheduler/scripts/docker.sh"]
