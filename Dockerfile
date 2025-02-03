FROM selenium/standalone-chrome AS builder

USER root

WORKDIR /tmp

COPY requirements.txt .
RUN apt update && \
    apt install -y wget vim git && \
    apt remove -y python3-pip && \
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py --break-system-packages && \
    apt clean && \
    rm -rf /var/cache/apt/archives /var/lib/apt/lists/*
RUN pip install --force --upgrade --break-system-packages --no-cache-dir -r requirements.txt


FROM builder AS runner
LABEL maintainer="naisanza@gmail.com"
LABEL description="autohotkey for websites"

WORKDIR /autositekey

COPY autositekey autositekey
COPY README.md .
COPY LICENSE .
COPY docker/entry.sh .

RUN chown -R ${SEL_UID}:${SEL_GID} .
USER ${SEL_UID}:${SEL_GID}

#CMD ["/bin/bash"]
ENTRYPOINT ["/bin/bash", "entry.sh"]
