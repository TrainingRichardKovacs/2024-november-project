FROM python:3.12-slim

# Frissítjük a csomaglistát és telepítjük a szükséges függőségeket
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Pip csomagok telepítése
RUN pip install --no-cache-dir sqlalchemy psycopg2-binary pandas

# Teszt parancs
CMD ["tail", "-f", "/dev/null"]
