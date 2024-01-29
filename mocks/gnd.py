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
