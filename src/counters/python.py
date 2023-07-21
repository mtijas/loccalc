supported_filetypes = ["py"]

def count_lines(file):
    total = 0
    loc = 0
    comments = 0
    empties = 0
    in_comment = False

    handle = open(file, 'r')
    for line in handle.readlines():
        total += 1

        stripped = line.strip()

        if not in_comment:
            if "" == stripped:
                empties += 1
            elif stripped.startswith(("'''", '"""')):
                if "'''" not in stripped[3:] and '"""' not in stripped[3:]:
                    in_comment = True
                comments += 1
            elif (stripped.startswith(("#"))):
                comments += 1
            else:
                loc += 1
        else:
            comments += 1
            if "'''" in stripped or '"""' in stripped:
                in_comment = False

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
