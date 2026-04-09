import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.DataFrame({
    'income': [20000,30000,50000,15000,60000,25000,40000],
    'credit': [600,650,750,500,800,700,720],
    'loan': [100000,150000,200000,50000,250000,120000,180000],
    'age': [22,25,30,19,40,28,35],
    'approved': [0,1,1,0,1,1,1]
})

X = data[['income','credit','loan','age']]
y = data['approved']

model = LogisticRegression()
model.fit(X,y)

pickle.dump(model, open('model.pkl','wb'))

print("Model trained successfully!")