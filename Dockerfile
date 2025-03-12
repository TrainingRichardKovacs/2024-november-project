FROM python:3.12-slim

COPY data /prooktatas/data
COPY data_loader /prooktatas/data_loader
COPY load_data.py /prooktatas/load_data.py

RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir sqlalchemy psycopg2-binary pandas

WORKDIR /prooktatas

CMD ["python", "load_data.py"]
    