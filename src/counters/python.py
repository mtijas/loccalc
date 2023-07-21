supported_filetypes = ["py"]

def count_lines(file):
    total = 0
    loc = 0
    comments = 0
    empties = 0
    in_comment = False
    starting_quotes = ""

    handle = open(file, 'r')
    for line in handle.readlines():
        total += 1

        stripped = line.strip()

        if not in_comment:
            if "" == stripped:
                empties += 1
            elif stripped.startswith(("'''", '"""', "#")):
                comments += 1
            else:
                loc += 1

            single_q_start = stripped.find("'''")
            double_q_start = stripped.find('"""')

            starting_quotes_position = -1

            if -1 < single_q_start and -1 < double_q_start:
                starting_quotes_position = min(single_q_start, double_q_start)
                starting_quotes = '"""' if starting_quotes_position == double_q_start else "'''"
            elif -1 < single_q_start:
                starting_quotes_position = single_q_start
                starting_quotes = "'''"
            elif -1 < double_q_start:
                starting_quotes_position = double_q_start
                starting_quotes = '"""'

            if (-1 < starting_quotes_position
                    and starting_quotes not in stripped[starting_quotes_position+3:]):
                in_comment = True

        else:
            comments += 1
            if starting_quotes in stripped:
                in_comment = False

    return {
        "comments": comments,
        "loc": loc,
        "empties": empties,
        "total": total,
    }
