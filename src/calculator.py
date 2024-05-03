import os
from .utils import types
from importlib import import_module
from src.visualizers import totals, by_filetype


def start(argv: list[str]):
    results = list()
    filetypes_to_counters = load_counters()

    for arg in argv:
        results.extend(count_dir(arg, filetypes_to_counters))

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
    file_path: str, filetypes_to_counters: dict[str, object]
) -> types.LineCount:
    filename = file_path.rsplit("/")[-1]
    if filename.startswith("."):
        return None

    filename_split = filename.rsplit(".")
    filetype = filename_split[-1] if len(filename_split) > 1 else "unknown"

    if filetype in filetypes_to_counters.keys():
        handler = filetypes_to_counters[filetype]
        linecount = types.LineCount(**handler.count_lines(file_path))
    else:
        linecount = None

    return types.ResultRow(
        path=filename.rsplit("/", 1)[0],
        filename=filename,
        filetype=filetype,
        linecount=linecount,
    )


def count_dir(
    dir_path: str, filetypes_to_counters: dict[str, object]
) -> list[types.ResultRow]:
    results = list()
    if os.path.isdir(dir_path):
        dir_path = dir_path.rstrip("/")
        try:
            items = os.listdir(dir_path)
        except PermissionError:
            return results

        for item in items:
            if item.startswith("."):
                continue

            full_path = f"{dir_path}/{item}"
            if os.path.isdir(full_path):
                results.extend(count_dir(f"{full_path}/", filetypes_to_counters))
            else:
                resultrow = handle_file(full_path, filetypes_to_counters)
                if resultrow is not None:
                    results.append(resultrow)

    elif os.path.isfile(dir_path):
        try:
            resultrow = handle_file(dir_path, filetypes_to_counters)
            if resultrow is not None:
                results.append(resultrow)
        except PermissionError:
            pass

    return results
