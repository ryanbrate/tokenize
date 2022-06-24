# tokenize

For each configuration defined in [tok_configs.json](tok_configs.json), perform en-masse tokenization of corpuses.

Each collection within a corpus is assumed to be of the form:

```
[
    [
        label,
        list of strings
    ],
    ...
]
```

The output collection is of the form:

```
[
    [
        label,
        list of token lists
    ],
    ...
]
```

## Performing tokenization

tokenize.py runs performs tokenization on each config in [tok_configs.json](tok_configs.json).

```python
python3 tok.py
```

### handling input data compatibility

* add a convert() function to [converters/](converters/), e.g., [converters.KB_sampling.convert](converters/KB_sampling.py)

* specify the correct "converter" in [tok_configs.json](tok_configs.json)

### choosing a lemmatizer (or reimplementing another)

* add a tokenize() function to [tokenizers/](tokenizers/spacy_tokenizer.py)

* specify the correct "lemmatizer" in [tok_configs.json](tok_configs.json)


### tok_configs.json options

* "input_dir": the dir holding the each collection in json format. Any files named "config.json" in this folder are ignored. 

* "output_dir": the dir to save tokenized versions of the collections in "samples_dir", saved with the save filename as .json files.

* "converter": the function used in the particular configuration to convert the format of the collections in "samples_dir" to the format assumed by the scripts.

* "tokenize": the function used to perform tokenization in each sample in a (converted) collection.

* "n_processes": number of parallel processes
