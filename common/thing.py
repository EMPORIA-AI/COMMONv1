#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from .base import *

class Thing(ObjectBase):

    #
    # 'thing_v1.0 abi
    #
    # : genre init-genre ;
    #

    """

    """

    id: str = ""
    acl: str = ""
    name: str = ""
    tags: str = ""

    vkey: str = ""

    genre_id: str = ""
    rpc_json: str = ""

    broker_id = ""
    holder_id = ""

    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'T'

