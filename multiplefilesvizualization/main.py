import pandas as pd
import matplotlib.pyplot as plt


data1 = pd.read_excel("shift-data.xlsx", sheet_name='first')
data2 = pd.read_excel("shift-data.xlsx", sheet_name='second')
data3 = pd.read_excel("third-shift-data.xlsx")

combined_data = pd.concat([data1, data2, data3])
shift_productivity = combined_data.groupby(["Shift"])[['Production Run Time (Min)', 'Products Produced (Units)']].mean()
shift_productivity.plot(kind='bar', stacked=True)

plt.xlabel('Shift')
plt.ylabel('Average Value')
plt.title('Production Metrics by Shift (Combined Data)')
plt.legend(title="Metric", loc='upper right')
plt.xticks(rotation=0)

plt.show()