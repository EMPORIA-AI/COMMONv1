#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from .base import *

#
# markets are managed as spaces where a combination of what and where.
#

class Space(ObjectBase):

    """

    """

    id: str = ""

    acl: str = ""
    name: str = ""
    tags: str = ""

    id_genre: str = ""
    id_where: str = ""

    program: str = ""
    storage: str = ""

    def verify(self, tables):

        results = []

        if not self.id_genre == "":
            if not self.id_genre in tables.genres:
                results.append([self, "id_genre key not able to be resolved"])

        if not self.id_where == "":
            if not self.id_where in tables.wheres:
                results.append([self, "id_where key not able to be resolved"])

        return results






