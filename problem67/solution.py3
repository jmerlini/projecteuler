def maxPath(filename)
    # opens file into f and sets an array for each number from top to bottom, left to right e.g. for [1,2,3], 2 would be 1's left child and 3 would be 1's right child.
    with open(filename, 'r') as f:
        myarray = [line.split() for line in f]
    
    # finds the number of lines in the file
    num_lines = sum(1 for line in open(filename, 'r'))

    # Starts at the second to last row and adds maximum child to that entry and propegates upwards.
    for k in range(0,num_lines - 1):
        for i in range(0,num_lines-k - 1):
            top_row = num_lines - k - 2
            bottom_row = num_lines - k - 1
            myarray[top_row][i] = int(myarray[top_row][i]) + max(int(myarray[bottom_row][i + 1]),int(myarray[bottom_row][i]))

    # returns maximal path sum
    return myarray[0][0]
