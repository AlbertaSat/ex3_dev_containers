#!/usr/bin/env python
from common import ADDRESSES, serve


class SimulatedSubsystems:
    def create_handler(self):
        def handle(conn):
            data = conn.recv(1024)
            if not data:
                return True
            print(data.decode('utf-8'), end='', flush=True)
            return False
        return handle


if __name__ == "__main__":
    sub = SimulatedSubsystems()
    serve(ADDRESSES['sub'][1], sub.create_handler())
