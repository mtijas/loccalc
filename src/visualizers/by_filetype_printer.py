from ..utils import types

def visualize(results):
    filetype_totals = {}

    for row in results:
        if row.filetype in filetype_totals:
            filetype_totals[row.filetype] = types.LineCount(
                loc = filetype_totals[row.filetype][1] + row.linecount.loc,
                comments = filetype_totals[row.filetype][1] + row.linecount.comments,
                empties = filetype_totals[row.filetype][1] + row.linecount.empties,
                total = filetype_totals[row.filetype][1] + row.linecount.total,
            )
        else:
            filetype_totals[row[2]] = row.linecount

    for key, linecount in filetype_totals.items():
        print(f"\n** {key} **")
        print(f"LOC: {linecount.loc}")
        print(f"Comments: {linecount.comments}")
        print(f"Empty rows: {linecount.empties}")
        print(f"Total: {linecount.total}")
