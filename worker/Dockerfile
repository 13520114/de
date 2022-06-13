FROM ubuntu:18.04

# Install required softwares
RUN apt upgrade -y && apt update -y && apt install -y wget

# Create a dedicated user
RUN useradd -ms /bin/bash danh
USER danh
WORKDIR /home/danh

# Install Miniconda and create a dedicated environment for Celery
RUN mkdir -p /home/danh/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /home/danh/miniconda3/miniconda.sh && \
    bash /home/danh/miniconda3/miniconda.sh -b -u -p /home/danh/miniconda3 && \
    rm -rf /home/danh/miniconda3/miniconda.sh && \
    /home/danh/miniconda3/bin/conda init bash && \
    /home/danh/miniconda3/bin/conda create --name de python=3.9 && \
    /home/danh/miniconda3/bin/conda install --name de -c conda-forge celery pika
