"""

Each passed tuple has the form ...
[
    label,
    # list of strings
]

Return a lemmatized version of the tuple of the form ...
[
    label,
    # list of sentences as token lists
]
"""

import spacy
nlp = spacy.load("nl_core_news_sm")


def tokenize(document: tuple) -> tuple:
    """

    Args:
        [
            label,
            # list of strings
        ]

    Return:
        [
            label,
            # list of sentences as token lists
        ]
    """

    label, list_of_strings = document

    sentences = []
    for s in list_of_strings:

        doc = nlp(s)
        for sent in doc.sents:
            tokens: list[str] = [t.text for t in sent]
            sentences.append(tokens)

    # finally:
    return (label, sentences)
