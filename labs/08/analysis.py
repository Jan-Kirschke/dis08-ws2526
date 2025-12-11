import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

"""
Palmer Penguins Dataset 
"""
print(str("="*90)+"\n\nPalmer Penguins Dataset Analysis\n\n"+str("="*90))

data_sets_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "data_sets")
df_peguins = pd.read_csv(filepath_or_buffer=os.path.join(data_sets_path, "penguins.csv"))

# Basic Statistics | Info | Null Values
print("Basic Statistics of Palmer Penguins Dataset:\n",df_peguins.describe())
print("Basic Information of Palmer Penguins Dataset:\n",df_peguins.info)
print("Nll Values in Palmer Penguins Dataset:\n",df_peguins.isnull().sum())

sns.boxplot(x='sex', y='flipper_length_mm', data=df_peguins)
plt.xlabel('Species')
plt.ylabel('Sepal Length')
plt.title('Boxplot of Sepal Length by Species')
plt.show()