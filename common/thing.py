#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from pydantic.dataclasses import dataclass
from decimal import *
import pendulum

from .base import *

@dataclass
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

    id_genre: str = ""
    rpc_json: str = ""

    program: str = ""
    storage: str = ""


