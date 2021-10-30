FROM python:3.5

ENV HOME /root
ENV PYTHONPATH "/usr/lib/python3/dist-packages:/usr/local/lib/python3.5/site-packages"
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get autoremove -y \
    && apt-get install -y \
        gcc \
        build-essential \
        zlib1g-dev \
        wget \
        unzip \
        cmake \
        python3-dev \
        gfortran \
        libblas-dev \
        liblapack-dev \
        libatlas-base-dev \
    && apt-get clean

RUN pip install --upgrade pip \
    && pip install \
        ipython[all] \
        numpy \
        nose \
        matplotlib \
        pandas \
        scipy \
        sympy \
        cython \
        cvxpy \
    && rm -fr /root/.cache

ENTRYPOINT [ "python" ]