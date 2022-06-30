import json
import multiprocessing
import pathlib
import re
import typing
from itertools import cycle, starmap

# load all converters
for p in pathlib.Path("converters").glob("*.py"):
    exec(f"import converters.{p.stem}")

# load all tokenizers
for p in pathlib.Path("tokenizers").glob("*.py"):
    exec(f"import tokenizers.{p.stem}")


def main():

    # ------
    # load the configs
    # ------
    with open("tok_configs.json", "r") as f:
        configs = json.load(f)

    # iterate over configs
    for config in configs:

        input_dir: pathlib.Path = (
            pathlib.Path(config["input_dir"]).expanduser().resolve()
        )
        output_dir: pathlib.Path = (
            pathlib.Path(config["output_dir"]).expanduser().resolve()
        )
        n_processes: int = int(config["n_processes"])

        if output_dir.exists():

            print(f"{output_dir} exists ... skipping")
            continue

        else:

            # create the output_dir
            output_dir.mkdir(exist_ok=True, parents=True)

            # iterable of sample ocr collection paths
            collections_paths: list[pathlib.Path] = [
                p for p in input_dir.glob("*.json") if p.stem != "config"
            ]

            # ------
            # create tokenized versions of each collection
            # ------

            # single process
            if n_processes == 1:

                for collection_path in collections_paths:
                    apply_to_collection(collection_path, config)

            # multiprocessing
            else:

                # iterable of (collection_path, config) tuples to be passed to
                # apply_to_collection()
                arguments: typing.Iterator[tuple] = zip(
                    collections_paths, cycle([config])
                )

                # run 
                pool = multiprocessing.Pool(n_processes)
                pool.starmap(apply_to_collection, arguments)


def apply_to_collection(collection_path: pathlib.Path, config: dict) -> None:
    """Apply converter, and then tokenizer to a collection and the save to
    config["output_dir"]
    """

    # load the config variables
    output_dir = pathlib.Path(config["output_dir"]).expanduser().resolve()
    convert: typing.Callable = eval(config["converter"])
    tok: typing.Callable = eval(config["tokenizer"])

    # load the collection
    with open(collection_path, "r") as f:
        collection = json.load(f) 

    # convert the collection to the format assumed by this script
    converted_collection = convert(collection)

    # get a tokenized version of the collection
    tokenized_collection = [tok(t) for t in converted_collection]

    # get the Path for where the tokenized collection will be sent
    collection_name: str = re.match(".*/(.+).json", str(collection_path)).groups()[0]

    # save
    with open(output_dir / f"{collection_name}.json", "w") as f:
        json.dump(tokenized_collection, f, indent=4, ensure_ascii=True)


if __name__ == "__main__":
    main()
