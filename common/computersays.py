#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

import os, copy

from cubed4th import FORTH

from dotenv import load_dotenv
load_dotenv(verbose=True)

class Agent(dict):

    def __init__(self, **kwargs):
        ...
        self.v = {}
        self.by_name = {}

    @staticmethod ### OS_GETENV ###
    def word_OS_under_GETENV__R_s3(e, t, c, s1, s2):
        return (os.getenv(s2, s1),)

    def load(self, name, code):

        self.e = FORTH.Engine("""

```

: id 'id ! ;

        """)

        self.e.Agent = Agent()
        self.e.import_lib(None, self.e.Agent)

        self.e.execute(code)

        self.v = self.e.root.memory
        self.by_name[name] = copy.copy(self.v)






