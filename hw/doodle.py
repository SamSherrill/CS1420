"""doodle.py

Generate ASCII-art tessellations (three selectable patterns).

Usage:
    python doodle.py <pattern> <rows> <cols>

pattern: 1, 2, or 3
rows: 1-10
cols: 1-10

The program validates inputs and prints error messages for invalid values.
Each pattern is printed in an ASCII tessellation (rows x cols).
Patterns are lightly colored using ANSI escape codes.
"""

import sys
from typing import List, Tuple


def get_patterns() -> Tuple[List[str], List[str], List[str], dict]:
    """Return three tile patterns (each as list of lines) and color map.

    Each tile uses the same number of lines so they tessellate easily.
    """
    # All tiles are 3 lines high for simplicity and easy tessellation.
    cat = [r" /\_/\ ", r"( o.o )", r" > ^ < "]

    tree = [r"  /\  ", r" /**\ ", r"  ||  "]

    fish = [r"<`)))><", r"  ( )  ", r"  / \  "]

    # ANSI color codes for each pattern (foreground). These are optional.
    colors = {1: "\033[93m", 2: "\033[92m", 3: "\033[96m"}  # yellow, green, cyan
    return cat, tree, fish, colors


def tessellate_tile(
    tile: List[str], rows: int, cols: int, sep: str = "  ", color: str = ""
) -> List[str]:
    """Return lines representing a tessellation of a single tile.

    - tile: list of strings (all same height)
    - rows, cols: number of tile repetitions
    - sep: separator between tiles horizontally
    - color: ANSI color code prefix (empty string for no color)
    """
    tile_height = len(tile)
    out_lines: List[str] = []

    reset = "\033[0m" if color else ""

    for r in range(rows):
        # For each line inside the tile height, build a row of repeated tiles
        for line_idx in range(tile_height):
            parts: List[str] = []
            for c in range(cols):
                parts.append(f"{color}{tile[line_idx]}{reset}")
            out_lines.append(sep.join(parts))

    return out_lines


def print_tessellation(pattern_id: int, rows: int, cols: int) -> None:
    """Print the selected pattern tessellated `rows` x `cols` times.

    pattern_id: 1..3
    rows, cols: positive ints (1-10 validated earlier)
    """
    cat, tree, fish, colors = get_patterns()
    tiles = {1: cat, 2: tree, 3: fish}

    tile = tiles[pattern_id]
    color = colors.get(pattern_id, "")
    lines = tessellate_tile(tile, rows, cols, sep="  ", color=color)

    for ln in lines:
        print(ln)


def validate_and_parse_args(argv: List[str]) -> Tuple[int, int, int]:
    """Validate and parse command-line arguments.

    Returns (pattern_id, rows, cols). Exits with a message on error.
    """
    if len(argv) != 4:
        print("Error: Usage: python doodle.py <pattern 1-3> <rows 1-10> <cols 1-10>")
        sys.exit(1)

    try:
        pattern = int(argv[1])
        rows = int(argv[2])
        cols = int(argv[3])
    except ValueError:
        print("Error: All arguments must be integers.")
        sys.exit(1)

    if pattern not in (1, 2, 3):
        print(f"Error: Pattern must be 1, 2, or 3. Found: {pattern}")
        sys.exit(1)

    if not (1 <= rows <= 10):
        print(f"Error: Rows must be between 1 and 10 inclusive. Found: {rows}")
        sys.exit(1)

    if not (1 <= cols <= 10):
        print(f"Error: Columns must be between 1 and 10 inclusive. Found: {cols}")
        sys.exit(1)

    return pattern, rows, cols


def main() -> None:
    """Main entry point for the doodle program."""
    pattern, rows, cols = validate_and_parse_args(sys.argv)
    print_tessellation(pattern, rows, cols)


if __name__ == "__main__":
    main()
