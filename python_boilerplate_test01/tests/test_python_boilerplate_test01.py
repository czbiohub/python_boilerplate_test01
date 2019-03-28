#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_python_boilerplate_test01
----------------------------------

Tests for `python_boilerplate_test01` module.
"""

import pytest


class TestPython_boilerplate_test01(object):

    def test___init__(self, one_hundred):
        assert 100 == one_hundred
