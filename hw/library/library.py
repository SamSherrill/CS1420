"""library.py

Process scrambled book files and produce a summarized, unscrambled output.

Usage:
    python library.py <input_file>

The input file must contain lines of the form:
    <text>|<line_number>
For example:
    "It was the best of times, it was the worst of times,"|1

The program will write a file named <CODE>_book.txt where <CODE> is the
three-letter stem of the input file (input file basename without extension).

Output format:
    - first line: the three-letter code
    - second line: Longest line (LINE_NUM): <content>
    - third line: Average length: <avg>
    - remaining lines: the book contents in correct line order

This module contains small, testable functions. Doctests are provided
for the parsing functions.
"""

from __future__ import annotations

import os
import sys
from typing import List, Tuple


def parse_record(record: str) -> Tuple[int, str]:
    """Parse a single record of the form '<text>|<line>' and return (line, text).

    The function splits at the last '|' to allow '|' inside the text if present.
    Surrounding double quotes around the text are removed if present.

    >>> parse_record('"Hello world"|3')
    (3, 'Hello world')
    >>> parse_record('NoQuotes here|1')
    (1, 'NoQuotes here')
    >>> parse_record('A|B|5')
    (5, 'A|B')
    """
    record = record.rstrip("\n")
    left, sep, right = record.rpartition("|")
    if sep == "":
        raise ValueError(f"Record missing separator '|': {record!r}")

    text = left.strip()
    # remove surrounding double quotes if present
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        text = text[1:-1]

    try:
        line_num = int(right.strip())
    except ValueError as exc:
        raise ValueError(f"Invalid line number in record: {record!r}") from exc

    return line_num, text


def process_records(
    records: List[str],
) -> Tuple[List[Tuple[int, str]], Tuple[int, str], int]:
    """Process raw record lines and return sorted lines, longest line, and average length.

    Returns:
      - sorted_records: list of (line_num, text) sorted ascending by line_num
      - longest: (line_num, text) chosen by maximum length; on tie choose later line_num
      - avg_len: average length rounded to nearest integer (0.5 rounds up)

    >>> recs = ['"a"|2', '"abc"|1']
    >>> sorted_lines, longest, avg = process_records(recs)
    >>> sorted_lines
    [(1, 'abc'), (2, 'a')]
    >>> longest
    (1, 'abc')
    >>> avg
    2
    """
    parsed: List[Tuple[int, str]] = [parse_record(r) for r in records]

    if not parsed:
        return [], (0, ""), 0

    # find longest: by (length, line_num) so tie-breaker prefers larger line_num
    longest = max(parsed, key=lambda it: (len(it[1]), it[0]))

    # average length (standard rounding: .5 rounds up)
    total = sum(len(text) for _, text in parsed)
    avg = int(total / len(parsed) + 0.5)

    sorted_records = sorted(parsed, key=lambda it: it[0])
    return sorted_records, longest, avg


def write_book_file(
    stem: str,
    longest: Tuple[int, str],
    avg: int,
    sorted_records: List[Tuple[int, str]],
    out_dir: str | None = None,
) -> str:
    """Write the output file named '<stem>_book.txt' and return the path.

    If `out_dir` is provided the file is written into that directory; otherwise
    it is written to the current working directory.
    """
    out_name = f"{stem}_book.txt"
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, out_name)
    else:
        out_path = out_name

    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(f"{stem}\n")
        line_num, text = longest
        fh.write(f"Longest line ({line_num}): {text}\n")
        fh.write(f"Average length: {avg}\n")
        for _, txt in sorted_records:
            fh.write(f"{txt}\n")

    return out_path


def process_file(path: str) -> str:
    """Process an input book file and produce the output file path.

    Raises FileNotFoundError if input does not exist.
    """
    # If path includes a directory component, use it as given. If the user
    # passed a bare filename, look for the file in the same directory as this
    # module (the library directory). Outputs are written into the module
    # directory as well.
    module_dir = os.path.dirname(__file__)
    if os.path.dirname(path):
        in_path = path
    else:
        in_path = os.path.join(module_dir, path)

    if not os.path.exists(in_path):
        raise FileNotFoundError(in_path)

    with open(in_path, "r", encoding="utf-8") as fh:
        records = fh.readlines()

    sorted_records, longest, avg = process_records(records)

    stem = os.path.splitext(os.path.basename(in_path))[0]
    out_path = write_book_file(stem, longest, avg, sorted_records, out_dir=module_dir)
    return out_path


def main(argv: List[str] | None = None) -> int:
    """Command-line entry point.

    Returns exit code (0 success, 1 error).
    """
    if argv is None:
        argv = sys.argv

    if len(argv) != 2:
        print("Usage: python library.py <input_file>")
        return 1

    path = argv[1]
    try:
        out = process_file(path)
    except FileNotFoundError:
        print(f"Error: file not found: {path}")
        return 1
    except ValueError as exc:
        print(f"Error processing file: {exc}")
        return 1

    print(f"Wrote: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
