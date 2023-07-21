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

import sys
from src import calculator
from src.visualizers import totals_printer

def main(argv):
    results = []

    for arg in argv:
        calculator.count_dir(arg, results)

    totals_printer.visualize(results)


if "__main__" == __name__:
    main(sys.argv[1:])
