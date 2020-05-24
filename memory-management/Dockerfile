FROM ubuntu:latest
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y bc
RUN apt-get install -y stress-ng
RUN mkdir /app
ADD . /app
ENTRYPOINT ["/app/memory-management-workload.sh"]
