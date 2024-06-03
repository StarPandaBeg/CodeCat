FROM python:3.10-alpine

COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir waitress

COPY . /app
CMD ["waitress-serve", "--port", "80", "app:app"]