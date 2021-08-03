__header__ = """

The AI's Marketplace (TAIM) <https://www.market.com.ai>

License (CC0-1.0) <https://spdx.org/licenses/CC0-1.0.html>

Copyright (c) 12021-12021 HE, Scott.McCallum@HQ.UrbaneINTER.NET

To the extent possible under law, Scott McCallum has waived all copyright
and related or neighboring rights to [ TAIM ]. This work is published
from <https://what3words.com/enablers.aromas.import>.

Commercial & Government entities must interact with ip@market.com.ai to
license the patents planned, pending and granted that this software
embodies. Individuals, Public Educational and Public Health Institutions
are irrevocably granted software/patent usage rights.

Lineage:

  Mostly built on cubed4th + pydantic



""" # __header__

from pydantic import BaseModel
from pydantic.dataclasses import dataclass, Union

from typing import Any, IO, Optional, List, Dict

from enum import Enum

from decimal import *

import pendulum

@dataclass
class Group:

    ulid: str
    link: str      = ""      # Link to the merged classification
    program: str   = """

'group_v1.0 schema

: main
'Drinks/Human major 'Energy/Sugar_Free minor
("Red Bull") brand 'ML unit 250 size 4 items
;

""".strip()

@dataclass
class Thing:
    ulid: str
    vkey: str                # Verifing key for later private communications

    group:         Group     # What is the thing is, in broad terms

    program: str   = """

'thing_v1.0 schema

: group init-group ;

""".strip()

#
#
#

@dataclass
class Schema_APIv01X:
    version:       str       # The SDK version
    timestamp:     str       # ISO8601 UTC time just before request was sent
    verifypem:     str       # The brokers ECDSA verify key PEM encoded
    id_market:     str       # Which instance does the SDK want

@dataclass
class Schema_DATAv01X:
    version:       str       # The CORE version
    timestamp:     str       # ISO8601 UTC time just before reply was sent
    verifypem:     str       # The markets ECDSA verify key PEM encoded
    id_handle:     str       # Compact ID for the identity this round
    aparatas:      str       # Entry url; ie. /1v0/MARKET/0.ENTER

# Price is seperated out from the programs as they cannot look at or change
# flow based on the value.  The market groups compatible sells and buys
# together and then "randomly" allows scripts where buy price is greater
# than sell price.

@dataclass
class Price:
    value:         Decimal = 1.0
    currency:      str = "AUD"
    decimals:      int = 2

# For each round brokers need to supply the rates they are offering to
# transform the price no-matter what currency is being used to price things
# Where the broker does not supply a cross rate, rates determined by the
# market will be used.

@dataclass
class Rate:
    primary: Price
    convert: List[Price]

#
#
#

@dataclass
class Enter_APIv01X:
    timestamp:     str
    id_handle:     str       # From the /SCHEMA call to ID the broker
    id_market:     str       # Which instance does the SDK want
    crossrate:     Union[None, List[Rate]] = None

@dataclass
class Enter_DATAv01X:
    timestamp:     str
    dwelltime:     int

# Charges, typically taxes and success fees on the exchange have access to
# pricing information.  By convention where taxes are applied after, the
# buyer agrees to pay these charges.  The cha

@dataclass
class Charge:
    ulid: str      = '01FBZGDKXHX75EFFJZQX1CZYC5'
    vkey: str      = "-- MARKET --" # Verifing key for later communications
    authority: str = "https://charges_1v0.api.market.com.au/api/1v0/charges"
    program: str   = """

'charge_v1.0 schema

: main apply-charge ;

'Charity/Oceans classification
<TRUE> is-optional 1.0 rate-percent
'https://seashepherd.org charge-url
'33VL8dzvoXbzshUWAPvrhiAiX3tBAdPPmL remit-btc

""".strip()


@dataclass
class Where:

    program = """

'where_1.0 schema

: main 'Earth planet 'AU country 'ACT state 'Braddon local ;

""".strip()

@dataclass
class Supply:
    ulid: str                #
    vkey: str                #

    price: Price             # Cannot be seen or manipulated by the program

    thing: Thing

    where: Where

    program: str   = """

'supply_v1.0 schema
: where init-where ;

: thing init-thing ;

""".strip()

@dataclass
class Demand:
    ulid:          str
    vkey:          str

    price:         Price     # The fixed price of how much to pay

    where:         Where     # Location calculate taxes/delivey/availability

    prog: str = """

'offer_v1.0 schema
: where init-where ;

: team init-team ;

: main ;

""".strip()


@dataclass
class Offer_APIv01X:
    timestamp:     str
    id_handle:     str
    demand:        Union[List[Demand], None]
    supply:        Union[List[Supply], None]

@dataclass
class Offer_DATAv01X:
    timestamp:     str

    # properly generated ulids should be unique. where they are not the market
    # may re-assign the sdk supplied values and any changes are noted in here
    ulid_swap:     Union[None, dict] = None


@dataclass
class Leave_APIv01X:
    timestamp:     str
    id_handle:     str

@dataclass
class Trade:
    supply_id:     Supply
    demand_id:     Demand
    charges:       Union[None, List[Charge]] = None
    supply_diags:  Union[None, dict] = None
    demand_diags:  Union[None, dict] = None

@dataclass
class Leave_DATAv01X:
    timestamp:     str
    demand:        List[Demand]
    supply:        List[Supply]
    trades:        List[Trade]


