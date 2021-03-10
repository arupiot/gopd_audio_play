FROM balenalib/raspberry-pi-debian-python:buster

RUN [ "cross-build-start" ]

# install dependencies
RUN sudo apt-get update && sudo apt-get -y install omxplayer

COPY play.py play.py
CMD ["python3", "play.py"]

RUN [ "cross-build-end" ]
