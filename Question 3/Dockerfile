FROM python:3.8-slim-buster

WORKDIR /my_codes 

RUN apt-get update \
    && apt-get install --yes --no-install-recommends \
    sudo gcc g++ nano ssh rsync sshpass \
    && rm -rf /var/lib/apt/lists/* && \
    python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir picamera RPi.GPIO

COPY . ./
COPY lib /opt/vc/lib
COPY 00-vmcs.conf /etc/ld.so.conf.d/00-vmcs.conf 

RUN ldconfig
#CMD ["bash", "dockerStartup.sh"]

