from .generic import generic_counter

supported_filetypes = ["j2"]

comment_block_delimiters = {
    "{#": "#}"
}

comment_starters = ()


def count_lines(file_path):
    return generic_counter(file_path, comment_block_delimiters, comment_starters)
