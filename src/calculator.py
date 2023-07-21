import os
from .utils import types

def handle_file(file, filetypes_to_counters):
    filetype = file.rsplit(".")[-1]
    if (filetype not in filetypes_to_counters.keys()):
        return

    handler = filetypes_to_counters[filetype]
    count_result = handler.count_lines(file)

    return types.LineCount(**count_result)

def count_dir(dir, results, filetypes_to_counters):
    if os.path.isdir(dir):
        dir = dir.rstrip("/")
        items = os.listdir(dir)
        for item in items:
            full_path = f"{dir}/{item}"
            if os.path.isdir(full_path):
                count_dir(f"{full_path}/", results, filetypes_to_counters)
            else:
                count_result = handle_file(full_path, filetypes_to_counters)
                if count_result is not None:
                    results.append(types.ResultRow(
                        path=dir,
                        filename=full_path.rsplit("/")[-1],
                        filetype=full_path.rsplit(".")[-1],
                        linecount=count_result
                    ))
    elif os.path.isfile(dir):
        count_result = handle_file(dir, filetypes_to_counters)
        if count_result is not None:
            results.append(types.ResultRow(
                path=dir.rsplit("/", 1)[0],
                filename=dir.rsplit("/")[-1],
                filetype=dir.rsplit(".")[-1],
                linecount=count_result
            ))
