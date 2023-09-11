#Importing Libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.svm import SVR

dataset = pd.read_csv('Data Analysis/dummy_data_hss.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values

Y = Y.reshape(len(Y),1)

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(X[:,:-1])
X[:, :-1] = imputer.transform(X[:, :-1])
imputer.fit(Y[:])
Y[:] = imputer.transform(Y[:])



#Using One Hot Encoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[3])],remainder='passthrough')
X = np.array(ct.fit_transform(X))

#Feature scaling
scaler_X = StandardScaler()
scaler_Y = StandardScaler()
X = scaler_X.fit_transform(X[:,:-1])
Y = scaler_Y.fit_transform(Y)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
#Training the SVR Model on the dataset
# regressor = SVR(kernel='rbf')
# regressor.fit(X,Y)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)    
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import r2_score
print(r2_score(y_test,y_pred,force_finite=False))