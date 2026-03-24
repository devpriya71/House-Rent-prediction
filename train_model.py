import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("house_rent.csv")

df = pd.DataFrame(data)
x = df.drop(labels=['Rent'],axis=1)
y = df['Rent']

model = LinearRegression()
model.fit(x,y)

pickle.dump(model,open('model.pkl','wb'))
print("Model trained & run")