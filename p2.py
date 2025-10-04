import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')

print(df.head())

#histogram
# df['SepalLengthCm'].plot.hist(bins =20, edgecolor = 'black')
# plt.show()

#scatter
# df.plot.scatter(x='PetalLengthCm',y='SepalLengthCm')
# plt.show()

# #pie 
# df['Species'].value_counts().plot.pie(autopct='%1.1f%%')
# plt.show()

#boxplot

# df['PetalLengthCm'].plot.box()
# plt.show()

#bar
# # Step 1: Group and calculate mean
# avg_petal = df.groupby("Species")["PetalLengthCm"].mean()

# # Step 2: Print results
# print(avg_petal)

# # Step 3: Plot as bar chart
# avg_petal.plot(kind="bar", title="Average Petal Length per Species")
# plt.show()


#license
df.plot(x='SepalLengthCm',y='PetalLengthCm',kind='line',marker='o')
plt.show()