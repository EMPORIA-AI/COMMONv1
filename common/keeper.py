#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0 & Additional T&Cs
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from .base import *

#
# alters, typically taxes and success fees on the exchange have access to
# pricing information.  by convention where taxes are applied after, the
# buyer agrees to pay these edits.
#

class Keeper(ObjectBase):

    #
    # 'keeper_v0.1 abi
    #
    #

    """


    """

    id: str = ""
    name: str = ""
    tags: str = ""

    vkey: str = ""

    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'K'
