#!/usr/bin/env python3
"""
Module Docstring
"""


def classifier(chunk):
    """..."""
    result = []
    models = [
        kw_classifier,
        phrase_classifier,
        fs_classifier
    ]
    for model in models:
        result.append( model(chunk) )

    return result


def kw_classifier(chunk):
    """..."""
    KEYWORDS = ['ill', 'sick', 'unemployed', 'child']

    result = {
        'search': 'KW',
        'target': None,
        'timestamp': None,
        'pred': None
        }
    for word in KEYWORDS:
        if word in chunk['text']:
            result['target'] = word
            result['timestamp'] = chunk['timestamp']
            result['pred'] = 1.0
            return result
    else:
        return None
    

def phrase_classifier(chunk):
    """..."""
    return None


def fs_classifier(chunk):
    """..."""

    from transformers import AutoModel

    result = {
        'search': 'FS',
        'target': None,
        'timestamp': None,
        'pred': None
        }
    model = AutoModel.from_pretrained("src/pretrained_models/finetuned--BAAI")
    probs = model.predict_prob(chunk['text'])
    if probs[1] > .5:
        result['target'] = chunk['text']
        result['timestamp'] = chunk['timestamp']
        result['pred'] = 1.0
        return result
    
    return None