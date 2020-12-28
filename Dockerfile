FROM python:3.8-alpine
WORKDIR /container
COPY requirements.txt requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "src/main.py"]
