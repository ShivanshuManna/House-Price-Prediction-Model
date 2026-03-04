import numpy as np
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression


np.random.seed(42)

X= pd.DataFrame({
    'Area': np.random.randint(500,1000,100),
    'Bedroom': np.random.randint(1,5,100),
    'age': np.random.randint(0,30,100)
})

y = X["Area"]*3000+X['Bedroom']-X['age']*1000

model= LinearRegression()
model.fit(X,y)

joblib.dump(model, 'model.pkl')
print("model is saved in model.pkl file")

