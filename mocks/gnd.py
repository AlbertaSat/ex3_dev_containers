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
    print(
        "EX3 Ground Station CLI v0.0.1\n"
        "Type anything to send to the Communications system."
    )
    while True:
        try:
            s = input("> ")
        except EOFError:
            break
        try:
            send_message(s)
        except Exception as e:
            print(e, file=sys.stderr)
