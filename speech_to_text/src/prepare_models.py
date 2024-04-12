#!/usr/bin/env python3
"""
Module Docstring

"""

from src import config_environment


def prepare():
    """..."""

    config_environment.config()

    #load model
    from setfit import SetFitModel

    model = SetFitModel.from_pretrained("BAAI/bge-small-en-v1.5")


    #get trainin records
    from datasets import load_dataset, Dataset

    train_records = [
        {'text': 'I was sick.',
         'label': 'positive'
         },
        {'text': 'My husband lost his job',
         'label': 'positive'
         },
         {'text': 'I got a raise at work',
         'label': 'negative'
         },
         {'text': 'I lost my dog to cancer',
         'label': 'negative'
         },
         ]
    #train_dataset = load_dataset(records)         #<<<FAILS HERE, maybe use this: Dataset.from_dict(
    train_dataset = Dataset.from_list(train_records)

    test_records = [
        {'text': "I got the flu and felt very bad.",
         'label': 'positive'
         },
        {'text': "I got a raise and feel great.",
         'label': 'negative'
         },
        {'text': "This bank is awful.",
         'label': 'negative'
         },
        {'text': 'He company laid him off.',
         'label': 'positive'
         },
         ]

    test_dataset = Dataset.from_list(test_records)
    model.labels = ["negative", "positive"]


    #train model
    from setfit import Trainer, TrainingArguments

    args = TrainingArguments(
        batch_size=32,
        num_epochs=10,
    )
    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_dataset,
    )
    trainer.train()




    #test model
    metrics = trainer.evaluate(test_dataset)
    print(metrics)
    '''
    preds = model.predict([
        "I got the flu and felt very bad.",
        "I got a raise and feel great.",
        "This bank is awful.",
        ])
    print(f'predictions: {preds}')
    '''
    model.save_pretrained("pretrained_models/finetuned--BAAI")     #TODO:ERROR - jinja2.exceptions.TemplateAssertionError: no test named 'False'

    return True