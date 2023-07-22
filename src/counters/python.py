from ..utils import search

supported_filetypes = ["py"]

def count_lines(file):
    total = 0
    loc = 0
    comments = 0
    empties = 0
    in_multiline_comment = False
    comment_start_str = None

    handle = open(file, 'r')
    for line in handle.readlines():
        total += 1

        stripped = line.strip()

        if not in_multiline_comment:
            if "" == stripped:
                empties += 1
            elif stripped.startswith(("'''", '"""', "#")):
                comments += 1
            else:
                loc += 1

            comment_start_str = search.find_multiline_starter(["'''", '"""'], stripped)
            if comment_start_str is not None:
                in_multiline_comment = True

        else:
            comments += 1
            ending_position = stripped.find(comment_start_str)
            if -1 < ending_position:
                comment_start_str = search.find_multiline_starter(["'''", '"""'], stripped[ending_position+3:])
                if comment_start_str is None:
                    in_multiline_comment = False

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
