FROM python:3.12-slim-bullseye AS builder

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt /backend/requirements.txt

RUN pip install --upgrade pip \
 && pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim-bullseye AS runtime
WORKDIR /backend

COPY --from=builder /install /usr/local

COPY /src /backend

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:create_app()"]
