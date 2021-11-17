import numpy as np
import pathlib


VALID_NUM_ROWS = [9]
VALID_NUM_COLS = [9]


def read(path: pathlib.Path) -> np.ndarray:
    """
    Reads a NxM sudoku puzzle into a numpy array.
    """
    try:
        array = np.loadtxt(path, dtype=str)
    except ValueError as e:
        raise ValueError(f"Error in the provided puzzle ({e})")

    if array.shape[0] not in VALID_NUM_ROWS or array.shape[1] not in VALID_NUM_COLS:
        raise NotImplementedError(
            f"A puzzle of shape {array.shape} is currently not supported"
        )

    return array


def write(array: np.ndarray, path: pathlib.Path) -> None:
    """
    Writes a puzzle's solution to file.
    """
    if not path.parent.is_dir():
        raise FileNotFoundError(
            f"Cannot find the directory to place the solution ('{path.parent}')"
        )

    np.savetxt(path, array, fmt="%s")
