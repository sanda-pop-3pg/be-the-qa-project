FROM python:3.6.4

WORKDIR /test-infrastructure
ADD . /test-infrastructure


RUN pip install -r docker/config/requirements.test.txt

SHELL ["/bin/bash", "-c"]

RUN mkdir /tmp/results

#ENTRYPOINT pytest -v -s --junit-xml=/tmp/results/results.xml
