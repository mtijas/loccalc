"""
Lines of Code calculator

Test by running `$ python3 loccalc.py manual-test`.

Should result:
** Totals **
LOC: 14
Comments: 55
Empty rows: 14
Total: 83

"""

import sys
import os
from importlib import import_module
from src import calculator
from src.visualizers import totals, by_filetype


def main(argv):
    results = []
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

    for arg in argv:
        calculator.count_dir(arg, results, filetypes_to_counters)

    by_filetype.visualize(results)
    totals.visualize(results)


if "__main__" == __name__:
    main(sys.argv[1:])
