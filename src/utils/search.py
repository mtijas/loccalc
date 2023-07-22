def find_multiline_starter(needles: list[str], haystack: str) -> str:
    """Finds the needle starting a multiline comment IF the haystack starts a multiline comment.

    Assumes block comments always end with the same needle/string they started with.

    Returns starting needle IF the haystack starts a multiline comment,
    None otherwise (the haystack closes all the comment blocks it starts).
    """
    found_substr = find_first_substr(needles, haystack)
    next_position = 0

    while found_substr is not None:
        comment_starting_needle = found_substr[0]
        # Find the next occurrence of same needle that started current comment block
        next_position += found_substr[1]+3
        found_substr = find_first_substr([found_substr[0]], haystack[next_position:])
        if found_substr is not None:
            # Current comment block ended (same needle found), let's find possible next block starter
            next_position += found_substr[1]+3
            found_substr = find_first_substr(needles, haystack[next_position:])
        else:
            # Current comment block continues till the end -> we are starting multiline comment
            return comment_starting_needle

    return None


def find_first_substr(needles: list[str], haystack: str) -> tuple[int, str]:
    """Finds the first occurrence of any needle in haystack and returns it and it's position
    as a tuple.
    """
    positions = list(zip(needles, map(haystack.find, needles)))
    positions = list(filter(lambda item: -1 < item[1], positions))
    if positions:
        return sorted(positions, key=lambda item: item[1])[0]
    else:
        return None
