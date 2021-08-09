__header__ = """

The AI's Marketplace (TAIM) <https://www.market.com.ai>

License (CC0-1.0) <https://spdx.org/licenses/CC0-1.0.html>

Copyright (c) 12021 - 12021 HE, Scott.McCallum@HQ.UrbaneINTER.NET

To the extent possible under law, Scott McCallum has waived all copyright
and related or neighboring rights to [ TAIM ]. This work is published
from <https://what3words.com/enablers.aromas.import> AU and SG.

Commercial & Government entities must interact with ip@market.com.ai to
license the patents planned, pending and granted that this software
embodies. Individuals, Public Educational and Public Health Institutions
are irrevocably granted software/patent usage rights.

Lineage:

  Mostly built on cubed4th + pydantic



""" # __header__

from typing import Any, IO, Optional, List, Dict
from pydantic.dataclasses import dataclass
from decimal import *
import pendulum

from .base import *

#
# markets are managed as spaces where a combination of what and where.
#

@dataclass
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