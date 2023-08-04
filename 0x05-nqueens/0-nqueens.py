#!/usr/bin/python3
"""
This module defines the NQueens class.
"""
import sys


class NQueens:
    """N queens solution finder class."""

    def __init__(self, n):
        """Initializes the NQueens class.

        Args:
            n (int): The size of the chessboard.
        """
        self.solutions = []
        self.n = n
        self.pos = list(map(lambda x: [x // n, x % n], range(n ** 2)))

    def is_attacking(self, pos0, pos1):
        """Checks if the positions of two queens are in an attacking mode.

        Args:
            pos0 (list or tuple): The first queen's position.
            pos1 (list or tuple): The second queen's position.

        Returns:
            bool: True if the queens are in an attacking position else False.
        """
        return (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]) or \
            abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

    def group_exists(self, group):
        """Checks if a group exists in the list of solutions.

        Args:
            group (list of integers): A group of possible positions.

        Returns:
            bool: True if it exists, otherwise False.
        """
        for stn in self.solutions:
            i = 0
            for stn_pos in stn:
                for grp_pos in group:
                    if stn_pos[0] == grp_pos[0] and stn_pos[1] == grp_pos[1]:
                        i += 1
            if i == self.n:
                return True
        return False

    def build_solution(self, row, group):
        """Builds a solution for the n queens problem.

        Args:
            row (int): The current row in the chessboard.
            group (list of lists of integers): The group of valid positions.
        """
        if row == self.n:
            tmp0 = group.copy()
            if not self.group_exists(tmp0):
                self.solutions.append(tmp0)
        else:
            for col in range(self.n):
                a = (row * self.n) + col
                matches = zip(list([self.pos[a]]) * len(group), group)
                used_positions = map(lambda x: self.is_attacking(
                    x[0], x[1]), matches)
                group.append(self.pos[a].copy())
                if not any(used_positions):
                    self.build_solution(row + 1, group)
                group.pop(len(group) - 1)

    def get_solutions(self):
        """Gets the solutions for the given chessboard size.
        """
        a = 0
        group = []
        self.build_solution(a, group)


def main():
    """Gets the solutions for the given chessboard size."""
    n = get_input()
    nq = NQueens(n)
    nq.get_solutions()
    for solution in nq.solutions:
        print(solution)


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    n = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


if __name__ == "__main__":
    main()
