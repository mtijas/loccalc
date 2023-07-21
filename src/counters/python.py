supported_filetypes = ["py"]

def count_lines(file):
    total = 0
    loc = 0
    comments = 0
    empties = 0

    handle = open(file, 'r')
    for line in handle.readlines():
        total += 1

        stripped = line.strip()

        if (stripped.startswith(("'"))):
            comments += 1
        elif "" == stripped:
            empties += 1
        else:
            loc += 1

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
