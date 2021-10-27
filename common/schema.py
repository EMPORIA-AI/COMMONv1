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

from .where import *
from .genre import *
from .space import *
from .thing import *
from .alter import *

# given parallel arrays of where the buyer is and the things they are needing
# the locate server will return a list of the urls where those markets are
# operating.  its expected that as the markets grow they will dynamically shard
# to achieve performance and saleability goals.

@dataclass
class Locate_APIv01X:
    id_wheres: List[str]
    id_genres: List[str]

@dataclass
class Locate_DATAv01X:
    engines: List[str]

#
#
#

@dataclass
class Setup_APIv01X:
    myversion: str  # the sdk version
    myedition: str  # config | supply | demand | trader | govern | observ
    timestamp: str  # iso8601 utc time just before request was sent
    verifykey: str  # the brokers ecdsa verify key encoded
    spaces_id: str  # which instance does the sdk want

@dataclass
class Setup_DATAv01X:
    myversion: str  # the core version
    timestamp: str  # iso8601 utc time
    verifykey: str  # the markets ecdsa verify key
    id_handle: str  # id for the identity this round
    next_path: str  # entry url; ie. /1v0/engines/0.enter

#
# Price is separated out from the programs as they cannot look at or change
# paths based on its value.  The market genres compatible sells and buys
# together and then "randomly" allows scripts where buy price is greater
# than sell price.
#

@dataclass
class Price:
    value: Decimal = 1.0
    currency: str = "AUD"
    decimals: int = 2

#
# For each round brokers need to supply the cross-rates they are offering to
# transform the price no-matter what currency is being used to price things.
# Where the broker does not supply a cross rate, rates determined by the
# market will be used.
#

@dataclass
class Rate:
    base: Price
    rate: List[Price]

#
#
#
#

@dataclass
class Supply:

    """

'supply_v1.0 abi

: where init-where ;

: thing init-thing ;

    """

    id: str = ""  # id assigned by the system
    acl: str = ""

    price: Optional[Price] = None

    id_thing: str = ""  # the id of the thing being sold
    id_where: str = ""  # where is item being sold from

    program: str = ""
    storage: str = ""

#
#
#
#



@dataclass
class Demand:

    """

'demand_v1.0 abi

: where init-where ;

: team init-team ;

: main ;

    """

    id: str = ""
    acl: str = ""
    vkey: str = ""  # ecdsa verifying key for later use

    id_where: str = ""  # location for taxes/delivery/availability

    price: Optional[Price] = None  # how much to pay if program says buy

    program: str = ""
    storage: str = ""

#
#
#
#


@dataclass
class Enter_APIv01X:
    timestamp: str
    spaces_id: str
    crossrate: List[Rate]


@dataclass
class Enter_DATAv01X:
    timestamp: str
    id_handle: str
    dwelltime: int
    next_path: str  # next path or none to loop

#
#
#
#

@dataclass
class Offer_APIv01X:
    timestamp: str
    id_handle: str
    demand: List[Demand]
    supply: List[Supply]

@dataclass
class Offer_DATAv01X:
    timestamp: str
    dwelltime: int

#
#
#
#

@dataclass
class Think_APIv01X:
    timestamp: str
    id_handle: str

@dataclass
class Think_DATAv01X:
    timestamp: str
    dwelltime: int


#
#
#
#

@dataclass
class Settle:
    supply_id: str = ""
    supply_diags: Optional[dict] = None
    demand_id: str = ""
    demand_diags: Optional[dict] = None
    alters: Optional[List[Alter]] = None

#
# leave is the final leg where the results of the round are passed to all the
# members, observers and governors of the round.  a closed boolean setting
# triggers the member to re-enter the market via the find/schema cycle when
# load re-balancing is being performed.
#

@dataclass
class Leave_APIv01X:
    timestamp: str
    id_handle: str

@dataclass
class Leave_DATAv01X:
    timestamp: str = ""
    demand: Optional[List[Demand]] = None
    supply: Optional[List[Supply]] = None
    settle: Optional[List[Settle]] = None

#
# the batching protocol allows for all the create, read, update and delete
# operations to be multiplexed over a single endpoint.
#

@dataclass
class Manage_APIv01X:
    action: Optional[Dict] = None
    genres: Optional[List[Genre]] = None
    wheres: Optional[List[Where]] = None
    spaces: Optional[List[Space]] = None
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None

@dataclass
class Manage_DATAv01X:
    result: Optional[Dict] = None
    genres: Optional[List[Genre]] = None
    wheres: Optional[List[Where]] = None
    spaces: Optional[List[Space]] = None
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None

