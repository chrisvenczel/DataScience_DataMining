import pandas as pd
import matplotlib.pyplot as plt

print("\n--- PROGRAM START ---\n")

df = pd.read_csv("Data/health_1.csv")
print(df)

df_wasting = df.groupby(['country_code', 'pervalence_of_wasting_male_children_under_5_percent'])
ax4 = df_wasting.plot(kind='line', figsize=(20,5))

print("\n--- PROGRAM COMPLETE ---\n")




