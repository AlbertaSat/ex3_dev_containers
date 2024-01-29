from python:3.10-alpine

WORKDIR /app

EXPOSE 5002

COPY common.py .

COPY sub.py .

CMD ["./sub.py"]
