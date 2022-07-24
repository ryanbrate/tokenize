"""

Each passed tuple has the form ...
[
    label,
    # list of strings
]

Return a tokenized version of the tuple of the form ...
[
    label,
    [
        [], # sentence as a list of tokens
        ...
    ]  # sentences
]
"""

import spacy
nlp = spacy.load("nl_core_news_sm")


def tokenize(document: tuple) -> tuple:
    """
    return tokenized (+lowercased) versions of input dataset

    Args:
        [
            label,
            # list of strings
        ]

    Return:
        [
            label,
            [
                [],  # a sentence as a list of tokens
                ...
            ]  # list of sentences as token lists
        ]

    by default, if list of strings is empty and to retain output consistency, return:
        [
            label, 
            [
                []
            ]
        ]
    """

    label, list_of_strings = document

    sentences = []

    if len(list_of_strings) == 0:  # empty list of strings
        sentences.append([])
    else:  # non-empty list of strings

        # add sentences, as lists of tokens, to sentences
        for s in list_of_strings:
            doc = nlp(s)
            for sent in doc.sents:
                tokens: list[str] = [t.text.lower() for t in sent]
                sentences.append(tokens)

    # finally:
    return (label, sentences)
