import numpy as np
import genetic
import test


def main():
    process = np.array([0, 5,  6, 16, 18, 7,  2, 14,  4, 9,
                       17, 1, 8, 11, 12, 10, 13, 3, 15, 19])
    a, b = genetic.layout(process)
    test.show_image()


main()
