def visualize(results):
    total_lines = 0
    total_loc = 0
    total_comments = 0
    total_empties = 0
    unknown_files = 0
    unknown_filetypes = set()

    for row in results:
        if row.linecount is None:
            unknown_files += 1
            unknown_filetypes.add(row.filetype)
            continue
        total_lines += row.linecount.total
        total_loc += row.linecount.loc
        total_comments += row.linecount.comments
        total_empties += row.linecount.empties

    print("\n** Totals **")
    print(f"LOC: {total_loc}")
    print(f"Comments: {total_comments}")
    print(f"Empty rows: {total_empties}")
    print(f"Total: {total_lines}")

    if unknown_files > 0:
        print(f"\n** Unknown files: {unknown_files} **")
        print(f"File types: {', '.join(unknown_filetypes)}")

