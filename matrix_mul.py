
# Example arrays 
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]

# Initialize an empty list to store the results
Ans = []

# Loop through each row in Prices
for i in range(len(Prices)):
    row_sum = 0  # Initialize the sum for the current row
    for j in range(len(Prices[i])):  # Loop through each element in the row
        row_sum += Prices[i][j] * Array2[j]  # Multiply corresponding elements and add to row_sum
    Ans.append(row_sum)  # Append the computed row sum to the result list

# Print the result
print(Ans)
