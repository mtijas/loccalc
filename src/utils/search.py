def find_multiline_starter(needles: dict[str, str], haystack: str) -> str:
    """Finds the needle starting a multiline comment IF the haystack starts a multiline comment.

    Expects needles to be a dict of block/multiline comment starting strings as keys and corresponding
    ending strings as values.

    Assumes block comments always end with the same needle/string they started with.

    Returns starting needle IF the haystack starts a multiline comment,
    None otherwise (the haystack closes all the comment blocks it starts).
    """
    found_substr = find_first_substr(needles.keys(), haystack)
    next_position = 0

    while found_substr is not None:
        comment_starting_needle = found_substr[0]
        # Find the closing occurrence for the needle that started current comment block
        next_position += found_substr[1]+3
        found_substr = find_first_substr([needles[found_substr[0]]], haystack[next_position:])
        if found_substr is not None:
            # Current comment block ended (same needle found), let's find possible next block starter
            next_position += found_substr[1]+3
            found_substr = find_first_substr(needles.keys(), haystack[next_position:])
        else:
            # Current comment block continues till the end -> we are starting multiline comment
            return comment_starting_needle

    return None


def find_first_substr(needles: list[str], haystack: str) -> tuple[int, str]:
    """Finds the first occurrence of any needle in haystack and returns it and it's position
    as a tuple.
    """
    needle_positions = list(zip(needles, map(haystack.find, needles)))
    actual_occurences = list(filter(lambda item: -1 < item[1], needle_positions))
    if actual_occurences:
        return sorted(actual_occurences, key=lambda item: item[1])[0]
    else:
        return None
