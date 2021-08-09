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
    start: int = 0
    count: int = 1000

@dataclass
class Locate_DATAv01X:
    space_ids: List[str]

#
#
#

@dataclass
class Schema_APIv01X:
    myversion: str  # the sdk version
    myedition: str  # config | supply | demand | govern | observ
    timestamp: str  # iso8601 utc time just before request was sent
    verifypem: str  # the brokers ecdsa verify key pem encoded
    id_market: str  # which instance does the sdk want

@dataclass
class Schema_DATAv01X:
    myversion: str  # the core version
    timestamp: str  # iso8601 utc time just before reply was sent
    verifypem: str  # the markets ecdsa verify key pem encoded
    id_handle: str  # id for the identity this round
    next_path: str  # entry url; ie. /1v0/market/0.enter

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

@dataclass
class Enter_APIv01X:
    id_market: str
    timestamp: str
    id_handle: str
    crossrates: List[Rate]

@dataclass
class Enter_DATAv01X:
    timestamp: str
    dwelltime: int
    next_path: str  # next path or none to loop


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
#


@dataclass
class Demand:

    """

'offer_v1.0 abi

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
    sharding: str = ""
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
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None
    spaces: Optional[List[Space]] = None

@dataclass
class Manage_DATAv01X:
    result: Optional[Dict] = None
    genres: Optional[List[Genre]] = None
    wheres: Optional[List[Where]] = None
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None
    spaces: Optional[List[Space]] = None

