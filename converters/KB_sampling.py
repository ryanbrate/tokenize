"""
The output from the KB_sampling/sample.py script is as follows:

# a json collection, resulting from a query
[
    # tuple of (ocr_name, ocr as a dict)
    [
        ocr_name,
        {
            "text": {
                "title": # str
                "p": # list[str] or str or null?
            }
        }
    ],
    ...
]

convert to collection to the form:
[
    # the converted tuple
    [
        ocr_name,
        [
            "some sentence",
            ...
        ]  # list of strings
    ],
    ...
]

"""

def convert(collection: list)->list:

    converted_collection = []

    for t in collection:

        ocr_name, ocr = t

        # get the list_of_strings
        if type(ocr["text"]["p"]) == str:
            list_of_strings = [ocr["text"]["p"]]
        elif type(ocr["text"]["p"]) == list: 
            list_of_strings = ocr["text"]["p"]
        else:
            list_of_strings = []

        converted_collection.append((ocr_name, list_of_strings))

    return converted_collection
