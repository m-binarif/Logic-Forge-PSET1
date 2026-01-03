def inventory_search(matrix, k):
    size = len(matrix)
    low = matrix[0][0]
    high = matrix[size - 1][size - 1]
    while low < high:
        guess = (low + high) // 2
        lighter_count = 0
        r = size - 1    
        c = 0
        while r >= 0 and c < size:
            if matrix[r][c] <= guess:
                lighter_count += r + 1
                c += 1
            else:
                r -= 1
        if lighter_count < k:
            low = guess + 1
        else:
            high = guess
    return low
inventory = [[1, 5, 9],[10, 11, 13],[12, 13, 15]]
print(inventory_search(inventory, 8))  
