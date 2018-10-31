def maxPath(filename)
    # opens file into f and sets an array for each number from top to bottom, left to right e.g. for [1,2,3], 2 would be 1's left child and 3 would be 1's right child.
    with open(filename, 'r') as f:
        myarray = [line.split() for line in f]

    # Starts at the second to last row and adds maximum child to that entry and propegates upwards.
    for k in range(0,99):
        for i in range(0,99-k):
            myarray[99-k-1][i] = int(myarray[99-k-1][i]) + max(int(myarray[99-k][i+1]),int(myarray[99-k][i]))

    # returns maximal path
    return myarray[0][0]
