from ..utils import search

supported_filetypes = ["c", "cpp", "h", "hpp"]

comment_block_delimiters = {
    "/*": "*/",
}

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
            if (stripped.startswith(("//", "/*", "*"))):
                comments += 1
            elif "" == stripped:
                empties += 1
            else:
                loc += 1

            comment_start_str = search.find_multiline_starter(comment_block_delimiters, stripped)
            if comment_start_str is not None:
                in_multiline_comment = True

        else:
            comments += 1
            ending_position = stripped.find(comment_block_delimiters[comment_start_str])
            if -1 < ending_position:
                comment_start_str = search.find_multiline_starter(
                    comment_block_delimiters,
                    stripped[ending_position+3:]
                )
                if comment_start_str is None:
                    in_multiline_comment = False

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
