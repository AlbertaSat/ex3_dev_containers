#!/usr/bin/env python
from common import ADDRESSES, Relay, serve


class FlightSoftware(Relay):
    def __init__(self):
        super().__init__(ADDRESSES['sub'])


if __name__ == "__main__":
    fsw = FlightSoftware()
    serve(ADDRESSES['fsw'][1], fsw.create_send_handler())
