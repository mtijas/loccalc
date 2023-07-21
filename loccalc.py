'''
Lines of Code calculator

Test by running `$ python3 loccalc.py test`. 

Should result:
**Totals**
LOC: 10
Comments: 30
Empty rows: 10
Total: 50

'''

import sys, os
from importlib import import_module
from src import calculator
from src.visualizers import totals_printer

def main(argv):
    results = []
    filetypes_to_counters = {}

    items = os.listdir("src/counters")
    for item in items:
        if item.startswith("_") or os.path.isdir(item):
            continue

        item = item.removesuffix(".py")
        instance = import_module(f"src.counters.{item}")
        for filetype in instance.supported_filetypes:
            filetypes_to_counters[filetype] = instance

    for arg in argv:
        calculator.count_dir(arg, results, filetypes_to_counters)

    totals_printer.visualize(results)


if "__main__" == __name__:
    main(sys.argv[1:])
