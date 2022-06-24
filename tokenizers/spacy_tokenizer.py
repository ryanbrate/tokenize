"""

Each passed tuple has the form ...
[
    label,
    # list of strings
]

Return a lemmatized version of the tuple of the form ...
[
    label,
    # list of lists of tokens
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
            # list of list of tokens
        ]
    """

    label, list_of_strings = document

    list_of_token_lists = []
    for s in list_of_strings:

        # convert the string into a string with lemmatized tokens
        doc = nlp(s)
        list_of_tokens: list[str] = [t.text for t in doc]

        # store
        list_of_token_lists.append(list_of_tokens)

    # finally:
    return (label, list_of_token_lists)
