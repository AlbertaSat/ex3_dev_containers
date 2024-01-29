#!/usr/bin/env python
from common import ADDRESSES, Relay, serve


class Comms(Relay):
    def __init__(self):
        super().__init__(ADDRESSES['fsw'])


if __name__ == "__main__":
    com = Comms()
    serve(ADDRESSES['com'][1], com.create_send_handler())

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
