#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from .base import *

class Genre(ObjectBase):

    #
    # 'genre_v1.0 abi
    #
    # : main
    # 'Drinks/Human major 'Energy/Sugar_Free minor
    # ("Red Bull") brand 'ML unit 250 size 4 count
    # ;
    #

    """

    """

    id: str = ""
    acl: str = ""
    name: str = ""
    tags: str = ""
    program: str = ""
    storage: str = ""

    def get_letter(self):
        return 'G'
