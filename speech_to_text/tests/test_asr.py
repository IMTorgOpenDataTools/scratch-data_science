#!/usr/bin/env python3
"""
Module Docstring
"""

from src import asr


def test_asr_workflow():
    tmp = asr.run_workflow()
    assert tmp == True



from src import prepare_models

def test_prepare_models():
    tmp = prepare_models.prepare()
    assert tmp == True
