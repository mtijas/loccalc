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
from src import calculator


def main(argv):
    calculator.start(argv)


if "__main__" == __name__:
    main(sys.argv[1:])
