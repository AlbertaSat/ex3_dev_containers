import socket
import sys
from typing import Callable

ADDRESSES: dict[str, tuple[str, int]] = {
    "com": ('com', 5000),
    "fsw": ('fsw', 5001),
    "sub": ('sub', 5002),
}


class Relay:
    def __init__(self, addr: tuple[str, int]):
        self.relay_conn = None
        self.relay_addr = addr

    def connect_to_relay(self):
        self.relay_conn = socket.create_connection(self.relay_addr)

    def close_conn(self):
        self.relay_conn.close()
        self.relay_conn = None

    def create_send_handler(self):
        def handle(conn):
            if self.relay_conn is None:
                self.connect_to_relay()
            data = conn.recv(1024)
            if not data:
                if self.relay_conn is not None:
                    self.close_conn()
                return True
            print(f"Got data: '{data.decode('utf-8').strip()}'")
            try:
                print(f"Sending to {self.relay_addr}")
                self.relay_conn.send(data)
            except Exception:
                self.close_conn()
            return False
        return handle


def serve(port: int, cb: Callable[[socket.socket], bool]):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('0.0.0.0', port))
        print(f'Listening on port {port}', file=sys.stderr)
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                while not cb(conn):
                    pass


__author__ = "Charles Ancheta"
__copyright__ = """
    Copyright (C) 2023, [Charles Ancheta]
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License."""
