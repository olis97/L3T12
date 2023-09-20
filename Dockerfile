FROM python:3.11
WORKDIR /app
COPY . /app
CMD python semantic.py

COPY requirements.txt /app

RUN python -m pip install --upgrade pip
RUN python -m pip install numpy

RUN pip install --no-cache-dir -r requirements.txt