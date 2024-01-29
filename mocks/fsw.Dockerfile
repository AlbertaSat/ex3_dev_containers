from python:3.10-alpine

WORKDIR /app

EXPOSE 5001

COPY common.py .

COPY fsw.py .

CMD ["./fsw.py"]
