#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0 & Additional T&Cs
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from .schema import *

import trio, asks, json

from pydantic.json import pydantic_encoder

from quart import abort

