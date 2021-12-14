#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: CC0-1.0 & Additional T&Cs
# Copyright (c) 12021 - 12021 HE, Emporia.AI Pte Ltd
# See LICENSE.md for Additional Terms and Conditions

from typing import Any, IO, Optional, List, Dict
from pydantic import BaseModel

class ObjectBase(BaseModel):

    def locate(action, database, factory, obj_name, objects):
        results = []
        for object in objects:
            results.append(object)
        return results

    def search(action, database, factory, obj_name, objects):
        results = []
        for object in objects:
            results.append(object)
        return results

    def verify(self, persist):
        return []

