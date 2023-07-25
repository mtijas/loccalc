from collections import namedtuple

LineCount = namedtuple(
    "LineCount", ["total", "loc", "comments", "empties"], defaults=[0, 0, 0, 0]
)

ResultRow = namedtuple("ResultRow", ["path", "filename", "filetype", "linecount"])
