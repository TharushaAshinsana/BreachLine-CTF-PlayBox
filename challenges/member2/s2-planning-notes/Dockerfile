FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y steghide libimage-exiftool-perl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /work
CMD ["/bin/bash"]