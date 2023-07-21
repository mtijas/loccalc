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

filetype_to_lang = {
    "java": "java",
    "c": "c",
    "h": "c",
    "cpp": "c",
    "hpp": "c",
    "py": "python",
}

lang_features = {
    "python": {
        "comments": ("'"),
    },
    "java": {
        "comments": ("//", "/*", "*", "*/"),
    },
    "c": {
        "comments": ("//", "/*", "*", "*/"),
    },
}

LineCount = namedtuple(
    "LineCount", 
    ["total", "loc", "comments", "empties"]
)

def count_lines(file, file_results):
    lines = 0
    loc = 0
    comments = 0
    empties = 0

    filetype = file.rsplit(".")[-1]
    if (filetype not in filetype_to_lang.keys()):
        return

    lang = filetype_to_lang[filetype]

    handle = open(file, 'r')
    for line in handle.readlines():
        lines += 1

        stripped = line.strip()

        if (stripped.startswith(lang_features[lang]["comments"])):
            comments += 1
        elif "" == stripped:
            empties += 1
        else:
            loc += 1

    result = LineCount(
        total=lines, 
        loc=loc, 
        comments=comments, 
        empties=empties
    )
    file_results.append((file, result))

def count_dir(dir, file_results):
    if os.path.isdir(dir):
        dir = dir.rstrip("/")
        items = os.listdir(dir)
        for item in items:
            if os.path.isdir(f"{dir}/{item}"):
                count_dir(f"{dir}/{item}/", file_results)
            else:
                count_lines(f"{dir}/{item}", file_results)
    elif os.path.isfile(dir):
        count_lines(dir, file_results)

def print_result(name, result):
    print(f"**{name}**")
    print(f"LOC: {result.loc}")
    print(f"Comments: {result.comments}")
    print(f"Empty rows: {result.empties}")
    print(f"Total: {result.total}")

def sum_totals(file_results):
    total_lines = 0
    total_loc = 0
    total_comments = 0
    total_empties = 0

    for row in file_results:
        total_lines += row[1].total
        total_loc += row[1].loc
        total_comments += row[1].comments
        total_empties += row[1].empties

    return LineCount(
        total=total_lines, 
        loc=total_loc, 
        comments=total_comments, 
        empties=total_empties
    )

def main(argv):
    file_results = []

    for arg in argv:
        count_dir(arg, file_results)

    for row in file_results:
        print_result(row[0], row[1])
        print("----------")

    totals = sum_totals(file_results)
    print_result("Totals", totals)


if "__main__" == __name__:
    main(sys.argv[1:])
