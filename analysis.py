import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Plot a simple graph
df.plot(kind='bar', x='Name', y='Age')
plt.show()
