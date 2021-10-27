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
class Where(ObjectBase):

    """

'where_1.0 abi

: main
'AU country 'NSW state 'Coolamon local
'///enablers.aromas.import w3w
;

    """

    id: str = ""
    acl: str = ""
    name: str = ""
    tags: str = ""
    program: str = ""
    storage: str = ""
