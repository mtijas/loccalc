from ..utils import search

def generic_counter(file_path: str, comment_block_delimiters: dict[str, str], comment_starters: tuple[str]) -> dict[str, int]:
    total = 0
    loc = 0
    comments = 0
    empties = 0
    comment_block_type = None

    handle = open(file_path, 'r')
    for line in handle.readlines():
        total += 1

        stripped = line.strip()

        if comment_block_type is None:
            if (stripped.startswith(comment_starters)):
                comments += 1
            elif "" == stripped:
                empties += 1
            else:
                loc += 1

            comment_block_type = search.find_multiline_starter(comment_block_delimiters, stripped)

        else:
            comments += 1
            ending_position = stripped.find(comment_block_delimiters[comment_block_type])
            if -1 < ending_position:
                comment_block_type = search.find_multiline_starter(
                    comment_block_delimiters,
                    stripped[ending_position+3:]
                )

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
