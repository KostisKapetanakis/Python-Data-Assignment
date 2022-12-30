import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("Assignment_table.csv")
df = pd.DataFrame(data)
x = df['zip_code']
y = df['bottles_sold']
plt.scatter(x, y, c=np.random.rand(len(x), 3))
plt.xlabel('Zip Code')
plt.ylabel('Bottles Sold')
plt.title('Bottles Sold')
plt.show()
