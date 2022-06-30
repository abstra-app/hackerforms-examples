FROM --platform=linux/x86_64 debian:11.3-slim
WORKDIR /app/

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-venv python3-distutils

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN ln -sf python3 /usr/bin/python && ln -sf pip3 /usr/bin/pip
RUN pip install --no-cache-dir --upgrade pip
RUN python -m venv $VIRTUAL_ENV

RUN pip install --no-cache-dir abstra-cli
COPY ./python ./python

ARG EXAMPLES_WORKSPACE_API_TOKEN
ENV ABSTRA_API_TOKEN $EXAMPLES_WORKSPACE_API_TOKEN

CMD abstra-cli upload ./python
