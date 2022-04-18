FROM debian:bullseye-slim

# Install python libs
RUN apt-get update && apt-get install -y \
    python-is-python3 \
    python3-pip \
    python3-wheel

ENV LANG=C.UTF-8

RUN useradd -m -d /home/appuser appuser
USER appuser
WORKDIR /app

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1                  \
    PYTHONDONTWRITEBYTECODE=1           \
    PIP_NO_CACHE_DIR=1                  \
    PIP_PROGRESS_BAR=off                \
    PIP_NO_COLOR=1                      \
    PIP_DISABLE_PIP_VERSION_CHECK=1     \
    PIP_USER=1

CMD ["bash"]

COPY --chown=appuser requirements.txt /tmp/requirements.txt
RUN pip install --user --no-cache-dir -r /tmp/requirements.txt && rm /tmp/requirements.txt

COPY --chown=appuser . .
