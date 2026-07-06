import numpy as np
import pandas as pd

# Create a Pandas Series from a Python list [10, 20, 30, 40] with custom index labels.
l1 = [10, 20, 30, 40]
labels = ['a', 'b', 'c', 'd']
d1 = {"A":10, "B":20, "C":30, "D":40, }
s1 = pd.Series(l1)
print(s1)

arr = np.random.randint(low=1, high=10, size=(5, 3))
print(arr)
data = pd.DataFrame(arr)
df = pd.DataFrame(arr, index=["1, "2", "3", "4", "5"], columns=[Name", "Age", "Marks])
print(df)