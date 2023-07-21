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
from collections import namedtuple

LineCount = namedtuple(
    "LineCount", 
    ["total", "loc", "comments", "empties"]
)

def countlines(file):
    lines = 0
    loc = 0
    comments = 0
    empties = 0

    handle = open(file, 'r')
    for line in handle.readlines():
        lines += 1

        stripped = line.strip()

        if (stripped.startswith("/*") 
                or stripped.startswith("*")
                or stripped.startswith("//")):
            comments += 1
        elif "" == stripped:
            empties += 1
        else:
            loc += 1

    return LineCount(
        total=lines, 
        loc=loc, 
        comments=comments, 
        empties=empties
    )

def count_dir(dir, file_results):
    dir = dir.rstrip("/")
    items = os.listdir(dir)
    for item in items:
        if os.path.isdir(f"{dir}/{item}"):
            count_dir(f"{dir}/{item}/", file_results)
        else:
            file_results.append((f"{dir}/{item}", countlines(f"{dir}/{item}")))

def print_result(name, result):
    print(f"**{name}**")
    print(f"LOC: {result.loc}")
    print(f"Comments: {result.comments}")
    print(f"Empty rows: {result.empties}")
    print(f"Total: {result.total}")

def main(argv):
    file_results = []
    total_lines = 0
    total_loc = 0
    total_comments = 0
    total_empties = 0

    for arg in argv:
        count_dir(arg, file_results)

    for row in file_results:
        print_result(row[0], row[1])
        print("----------")
        total_lines += row[1].total
        total_loc += row[1].loc
        total_comments += row[1].comments
        total_empties += row[1].empties

    totals = LineCount(total_lines, total_loc, total_comments, total_empties)
    print_result("Totals", totals)


if "__main__" == __name__:
    main(sys.argv[1:])
