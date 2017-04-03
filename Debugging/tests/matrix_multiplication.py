def matrix_multiply(a, b):
    def entry_sum(row, col):
        # Calculate the value of an individual entry in the resultant matrix,
        # given the row and column indices of the entry
        this_sum = 0

        i = 0
        for num in a[row]:
            this_sum += num * b[i][col]
            i += 1

        return this_sum
        
    # For every row in the original matrix, add a row to the new matrix
    result = [list() for row in a]
    
    # Populate matrix with results
    r = 0
    for row in result:
        # Populate columns
        c = 0
        for col in a[1]:
            row.append(entry_sum(r, c))
            c += 1
            
        r += 1
    
    return(result)