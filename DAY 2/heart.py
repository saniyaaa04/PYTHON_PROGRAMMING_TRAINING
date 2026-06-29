for row in range(6):
    for col in range(7):
        # Mathematical condition to form the upper curves and lower V-shape
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or \
           (row + col == 8):
            print("*", end=" ")
        elif (row == 1 and col in [1, 2, 4, 5]) or \
             (row == 2 and col in [1, 2, 3, 4, 5]) or \
             (row == 3 and col in [2, 3, 4]) or \
             (row == 4 and col == 3):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()