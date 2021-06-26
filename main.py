import pandas as pd
import numpy as np
import matplotlib_inline  as plt
import matplotlib.pyplot as plt
from sklearn import linear_model
n = int(input("Enter the area square feet: "))
df  = pd.read_csv("price_of_land.csv")
plt.xlabel('Area')
plt.ylabel('Price')
plt.scatter(df.area, df.price, color = 'red', marker= '*')
reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
price_answer = reg.predict([[n]])
print(price_answer)
