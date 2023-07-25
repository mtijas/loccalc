import os
from .utils import types
from importlib import import_module
from src.visualizers import totals, by_filetype


def start(argv: list[str]):
    filetypes_to_counters = load_counters()

    for arg in argv:
        results = count_dir(arg, filetypes_to_counters)

    by_filetype.visualize(results)
    totals.visualize(results)


def load_counters() -> dict[str, object]:
    filetypes_to_counters = {}

    items = os.listdir("src/counters")
    for item in items:
        if os.path.isdir(item) or item.startswith("_") or not item.endswith(".py"):
            continue

        item = item.removesuffix(".py")
        instance = import_module(f"src.counters.{item}")
        if hasattr(instance, "supported_filetypes"):
            for filetype in instance.supported_filetypes:
                filetypes_to_counters[filetype] = instance

    return filetypes_to_counters


def handle_file(
    file_name: str, filetypes_to_counters: dict[str, object]
) -> types.LineCount:
    filetype = file_name.rsplit(".")[-1]
    if filetype not in filetypes_to_counters.keys():
        return

    handler = filetypes_to_counters[filetype]
    count_result = handler.count_lines(file_name)

    return types.LineCount(**count_result)


def count_dir(
    dir_path: str, filetypes_to_counters: dict[str, object]
) -> list[types.ResultRow]:
    results = list()
    if os.path.isdir(dir_path):
        dir_path = dir_path.rstrip("/")
        items = os.listdir(dir_path)

        for item in items:
            full_path = f"{dir_path}/{item}"
            if os.path.isdir(full_path):
                results.extend(count_dir(f"{full_path}/", filetypes_to_counters))
            else:
                count_result = handle_file(full_path, filetypes_to_counters)
                if count_result is not None:
                    results.append(
                        types.ResultRow(
                            path=dir_path,
                            filename=full_path.rsplit("/")[-1],
                            filetype=full_path.rsplit(".")[-1],
                            linecount=count_result,
                        )
                    )

    elif os.path.isfile(dir_path):
        count_result = handle_file(dir_path, filetypes_to_counters)
        if count_result is not None:
            results.append(
                types.ResultRow(
                    path=dir_path.rsplit("/", 1)[0],
                    filename=dir_path.rsplit("/")[-1],
                    filetype=dir_path.rsplit(".")[-1],
                    linecount=count_result,
                )
            )

    return results
