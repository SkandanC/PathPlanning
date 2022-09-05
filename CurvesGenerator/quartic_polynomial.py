"""
Quartic Polynomial
"""

import numpy as np


class QuarticPolynomial:
    def __init__(self, x0, v0, a0, v1, a1, T):
        A = np.array([[3 * T ** 2, 4 * T ** 3],
                      [6 * T, 12 * T ** 2]])
        b = np.array([v1 - v0 - a0 * T,
                      a1 - a0])
        X = np.linalg.solve(A, b)

        self.a0 = x0
        self.a1 = v0
        self.a2 = a0 / 2.0
        self.a3 = X[0]
        self.a4 = X[1]

    def calc_xt(self, t):
        return (
            self.a0
            + self.a1 * t
            + self.a2 * t**2
            + self.a3 * t**3
            + self.a4 * t**4
        )

    def calc_dxt(self, t):
        return (
            self.a1 + 2 * self.a2 * t + 3 * self.a3 * t**2 + 4 * self.a4 * t**3
        )

    def calc_ddxt(self, t):
        return 2 * self.a2 + 6 * self.a3 * t + 12 * self.a4 * t ** 2

    def calc_dddxt(self, t):
        return 6 * self.a3 + 24 * self.a4 * t

