import argparse
import pathlib

from decrypter.helpers import puzzle_parser, printer
from decrypter import solver


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description="Solves a given sudoku puzzle; can be traditional or contain special rules (see README.md for help with encoding puzzle).")
    # parser.add_argument("--path", "-p", help="Puzzle path (.txt)")
    # parser.add_argument("--verbose", "-v", required=False, help="Print puzzle before and after solving")
    # args = parser.parse_args()

    puzzle_path = (
        pathlib.Path(__file__).absolute().parents[0]
        / "tests/puzzles/traditional/easy.txt"
    )  # pathlib.Path(args.path)
    verbose = False  # args.verbose
    if not puzzle_path.is_file():
        raise FileNotFoundError(f"Cannot find the puzzle ('{puzzle_path}')")

    # Read in puzzle
    puzzle = puzzle_parser.read(puzzle_path)
    if verbose:
        printer.print_table(puzzle)

    # Solve puzzle
    solution = solver.solve(puzzle)

    # Write solution to file
    solution_path = puzzle_path.parent / f"{puzzle_path.stem}_solved.txt"
    # puzzle_parser.write(solution, solution_path)
    if verbose:
        printer.print_table(solution)
