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
from enum import Enum

class Scope(Enum):
    Galaxy = 1
    Planet = 2
    Country = 3
    State = 4
    City = 5
    Suburb = 6

scopes = []
for scope in Scope:
    scopes.append(str(scope)[6:])

print("scopes = ", scopes)

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
    scope: str = ""
    id_up: str = ""
    program: str = ""
    storage: str = ""

    def verify(self, tables):

        results = []

        if not self.id_up == "":
            if not self.id_up in tables.wheres:
                results.append([self, "id_up key not able to be resolved"])

        if not self.scope == "":
            if not self.scope in scopes:
                results.append([self, "scope is not on suppoted list"])

        return results

