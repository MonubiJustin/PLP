import pandas as pd     # For data manipulation
import numpy as np      # For numerical operations
import matplotlib.pyplot as plt     # For data visualisation
import requests     # For making web requests

# Create a Numpy array of numbers from 1 to 10 and calculate the mean
arr = np.arange(1, 11) 
mean_value = np.mean(arr)
print("Numpy Array: ", arr)
print("Mean Value: ", mean_value)

# Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, 30, 35, 40, 45],
    "Salary": [50_000, 60_000, 70_000, 80_000, 90_000]
}

df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# Fetch data from a public API requests and print a key piece of information
response = requests.get("https://api.github.com")

if response.status_code == 200:
    github_data = response.json()
    print(f"\nGitHub API Message: {github_data['current_user_url']}")
else:
    print("\nFailed to fetch data from GitHub API.")
    
# Plot a simple line graph using matplotlib
numbers = [1, 2, 3, 4, 5]
plt.plot(numbers, [n**2 for n in numbers], marker='o')
plt.title("Number vs. Square")
plt.xlabel("Number")
plt.ylabel("Square")
plt.grid(True)
plt.show()