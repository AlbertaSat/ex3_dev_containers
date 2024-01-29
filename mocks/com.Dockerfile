from python:3.10-alpine

WORKDIR /app

EXPOSE 5000

COPY common.py .

COPY com.py .

CMD ["./com.py"]
