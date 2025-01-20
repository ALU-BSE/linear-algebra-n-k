# Example arrays
Prices = [[300, 500],  
          [1000, 120.85]]  # 2x2 matrix representing prices of two items

Array2 = [200, 100]  # A list that contains quantities of the items

# Initialize an empty list to store the results
Ans = []

# Iterate over each row in the Prices matrix
for i in range(len(Prices)):
    row_sum = 0  # To store the sum of products for the current row
    
    # Iterate over each element in the current row of Prices
    for j in range(len(Prices[0])):
        # Multiply corresponding element in the row with the element in Array2
        row_sum += Prices[i][j] * Array2[j]
    
    # Append the computed row_sum (dot product for the current row) to the Ans list
    Ans.append(row_sum)

# Print the result which will contain the dot products
print(Ans)
