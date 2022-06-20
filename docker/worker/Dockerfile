FROM ubuntu:18.04

# Variables
ARG USERNAME=${USERNAME:-danh}
ARG HOME_DIR=/home/${USERNAME:-danh}
ARG CONDA_DIR=${HOME_DIR}/miniconda3
ARG CONDA_SCRIPT_URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

# Install required softwares
RUN apt upgrade -y && \
    apt update -y && \
    apt install -y wget

# Create a dedicated user
RUN useradd -ms /bin/bash ${USERNAME}
USER ${USERNAME}
WORKDIR ${HOME_DIR}

# Install Miniconda and create a dedicated environment for Celery
RUN mkdir -p ${CONDA_DIR} && \
    wget ${CONDA_SCRIPT_URL} -O ${CONDA_DIR}/miniconda.sh && \
    bash ${CONDA_DIR}/miniconda.sh -b -u -p ${CONDA_DIR} && \
    rm -rf ${CONDA_DIR}/miniconda.sh && \
    ${CONDA_DIR}/bin/conda init bash && \
    ${CONDA_DIR}/bin/conda create --name de python=3.9

SHELL ["/bin/bash", "-ec"]

# Install Celery libraries and its required other libs
RUN source ${CONDA_DIR}/bin/activate && \
    conda activate de && \
    pip install "celery[librabbitmq,redis,auth,msgpack]" psycopg2-binary SQLAlchemy

# Change default command to keep container alive
CMD ["tail", "-F", "anything"]
