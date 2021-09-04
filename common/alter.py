__header__ = """

The AI's Marketplace (TAIM) <https://www.emporia.ai>

License (CC0-1.0) <https://spdx.org/licenses/CC0-1.0.html>

Copyright (c) 12021 - 12021 HE, Scott.McCallum@HQ.UrbaneINTER.NET

To the extent possible under law, Scott McCallum has waived all copyright
and related or neighboring rights to [ TAIM ]. This work is published
from <https://what3words.com/enablers.aromas.import> AU and SG.

Commercial & Government entities must interact with ip@emporia.ai to
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
# alters, typically taxes and success fees on the exchange have access to
# pricing information.  by convention where taxes are applied after, the
# buyer agrees to pay these edits.
#

@dataclass
class Alter(ObjectBase):

    #
    # 'alter_v1.0 abi
    #
    # : main apply-alter ;
    #
    # 'Charity/Oceans classification
    # <TRUE> is-optional 1.0 rate-percent
    # 'https://seashepherd.org charge-url
    # '33VL8dzvoXbzshUWAPvrhiAiX3tBAdPPmL remit-btc
    #

    """


    """

    id: str = ""
    acl: str = ""
    name: str = ""
    tags: str = ""

    vkey: str = ""

    program: str = ""
    storage: str = ""
