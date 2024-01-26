#!/usr/bin/env python
import socket
import sys

from common import ADDRESSES


def send_message(msg: str):
    print(f"Sending '{msg}'", file=sys.stderr)
    conn = socket.create_connection(ADDRESSES['com'])
    conn.send((msg + '\n').encode('utf-8'))
    conn.close()


if __name__ == "__main__":
    while True:
        send_message(input("> "))
