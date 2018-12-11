#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
module docs
"""
import re

SEARCH_URL = "https://cht.sh/"

ANSI_ESCAPE = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')
