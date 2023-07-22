from .generic import generic_counter

supported_filetypes = ["py"]

comment_block_delimiters = {
    "'''": "'''",
    '"""': '"""',
}

comment_starters = ("'''", '"""', "#")

def count_lines(file):
    return generic_counter(file, comment_block_delimiters, comment_starters)
