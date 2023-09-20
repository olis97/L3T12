FROM pypy:latest
WORKDIR /app
COPY . /app
CMD python semantic.py
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt
