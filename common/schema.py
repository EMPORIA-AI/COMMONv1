#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0 & Additional T&Cs
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from pydantic.dataclasses import dataclass
from decimal import *

import pendulum

from .base import *

from .value import *
from .where import *
from .genre import *
from .space import *
from .thing import *
from .alter import *

from .broker import *
from .keeper import *

# given parallel arrays of where the buyer is and the things they are needing
# the locate server will return a list of the urls where those markets are
# operating.  its expected that as the markets grow they will dynamically shard
# to achieve performance and saleability goals.

@dataclass
class Locate_DATA:
    where_ids: List[str]
    genre_ids: List[str]

@dataclass
class Locate:
    engines: List[str]

#
#
#

@dataclass
class Setup_DATA:
    clock: str = "" # iso8601 utc time just before request was sent
    version: str = ""  # the sdk version
    edition: str = ""  # config | supply | demand | trader | govern | observ
    space_id: str = ""  # which instance does the sdk want
    broker_id: str = ""
    vkey: str = "" # the brokers ecdsa verify key encoded

@dataclass
class Setup:
    clock: str = "" # iso8601 utc time
    handle: str = "" # id for the identity this round
    version: str = ""  # the core version
    dwell: int = 0  # how long should the client wait
    vkey: str = ""  # the markets ecdsa verify key

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

    price: Optional[Price] = None

    thing_id: str = ""  # the id of the thing being sold
    where_id: str = ""  # where is item being sold from

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
    vkey: str = ""  # ecdsa verifying key for later use

    where_id: str = ""  # location for taxes/delivery/availability

    price: Optional[Price] = None  # how much to pay if program says buy

    program: str = ""
    storage: str = ""

#
#
#
#


@dataclass
class Enter_DATA:
    clock: str = ""
    handle: str = ""
    crossrate: Optional[List[Rate]] = None


@dataclass
class Enter:
    clock: str = ""
    dwell: int = 0

#
#
#
#

@dataclass
class Offer_DATA:
    clock: str = ""
    handle: str = ""
    demand: Optional[List[Demand]] = None
    supply: Optional[List[Supply]] = None

@dataclass
class Offer:
    clock: str = ""
    dwell: int = 0

#
#
#
#

@dataclass
class Think_DATA:
    clock: str = ""
    handle: str = ""

@dataclass
class Think:
    clock: str = ""
    dwell: int = 0


#
#
#
#

@dataclass
class Settle:
    thing: Optional[Thing] = None
    supply: Optional[Supply] = None
    demand: Optional[Demand] = None
    alters: Optional[List[Alter]] = None
    choices: Optional[dict] = None

#
# leave is the final leg where the results of the round are passed to all the
# members, observers and governors of the round.  a closed boolean setting
# triggers the member to re-enter the market via the find/schema cycle when
# load re-balancing is being performed.
#

@dataclass
class Leave_DATA:
    clock: str = ""
    handle: str = ""

@dataclass
class Leave:
    clock: str = ""
    dwell: int = 0
    settle: Optional[List[Settle]] = None

#
# the batching protocol allows for all the create, read, update and delete
# operations to be multiplexed over a single endpoint.
#

@dataclass
class Manage_DATA:
    action: Optional[Dict] = None
    values: Optional[List[Value]] = None
    genres: Optional[List[Genre]] = None
    wheres: Optional[List[Where]] = None
    spaces: Optional[List[Space]] = None
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None
    brokers: Optional[List[Broker]] = None
    keepers: Optional[List[Keeper]] = None

@dataclass
class Manage:
    result: Optional[Dict] = None
    values: Optional[List[Value]] = None
    genres: Optional[List[Genre]] = None
    wheres: Optional[List[Where]] = None
    spaces: Optional[List[Space]] = None
    things: Optional[List[Thing]] = None
    alters: Optional[List[Alter]] = None
    brokers: Optional[List[Broker]] = None
    keepers: Optional[List[Keeper]] = None

