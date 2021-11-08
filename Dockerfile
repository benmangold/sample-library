FROM python:3.8.5

RUN apt-get update; apt-get install make jq --yes; useradd python; mkdir -p /home/python/app; chown -R python /home/python;

WORKDIR /home/python/app

USER python

RUN pip install black

ENTRYPOINT [ "/bin/bash" ]
