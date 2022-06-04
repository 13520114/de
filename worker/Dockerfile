FROM ubuntu:18.04

# Install required softwares
RUN apt upgrade -y && apt update -y && apt install -y wget

# Install Miniconda and create a dedicated environment for Celery
RUN mkdir -p /root/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /root/miniconda3/miniconda.sh && \
    bash /root/miniconda3/miniconda.sh -b -u -p /root/miniconda3 && \
    rm -rf /root/miniconda3/miniconda.sh && \
    /root/miniconda3/bin/conda init bash && \
    /root/miniconda3/bin/conda create --name de python=3.9 && \
    /root/miniconda3/bin/conda install --name de -c conda-forge celery
