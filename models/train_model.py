import pandas as pd
import csv
import joblib #saves model to file

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv("data/dataset/sign_data.csv",header=None)

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42)

model = RandomForestClassifier(n_estimators=200)

model.fit(x_train,y_train)

predictions = model.predict(x_test)

accuracy = accuracy_score(y_test,predictions)

print(f"\nAccuracy: {accuracy * 100:.2f}%\n")

joblib.dump(
    model,
    "models/classifier.pkl"
)

print("Model trained and saved.")