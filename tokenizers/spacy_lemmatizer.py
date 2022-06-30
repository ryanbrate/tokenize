"""

Each passed tuple has the form ...
[
    label,
    # list of strings
]

Return a lemmatized & tokenized version of the tuple of the form ...
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
            tokens: list[str] = [t.lemma_ for t in sent]
            sentences.append(tokens)

    # finally:
    return (label, sentences)
