import pandas as pd
import numpy as np

# Load data
data = pd.read_csv('path/to/data')

# Example arrays
Prices = [[300, 500],
          [1000, 120.85]]

Array2 = [200, 100]  # A list that contains quantities of the items

# Initialize an empty list to store the results
Ans = []

for i in range(len(Prices)):
    row_sum = 0
    for j in range(len(Prices[0])):
        # COMPLETE THE MISSING LOGIC HERE
        pass


print(Ans)
