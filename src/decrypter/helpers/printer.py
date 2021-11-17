from tabulate import tabulate
import numpy as np


def print_table(table: np.ndarray) -> None:
    print(tabulate(table[:3], tablefmt="fancy_grid"))
    print(tabulate(table[3:6], tablefmt="fancy_grid"))
    print(tabulate(table[6:], tablefmt="fancy_grid"))
