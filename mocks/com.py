#!/usr/bin/env python
from common import ADDRESSES, Relay, serve


class Comms(Relay):
    def __init__(self):
        super().__init__(ADDRESSES['fsw'])


if __name__ == "__main__":
    com = Comms()
    serve(ADDRESSES['com'][1], com.create_send_handler())
