# Importing the library

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

 # Importing data
 
dataset = pd.read_csv("Data.csv")
 
X= dataset.iloc[:,:-1].values
Y= dataset.iloc[:,-1].values
 
 # Taking care of missing data
 
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy='mean',axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

#Categorical Data

from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
labelEncoder_X = LabelEncoder()
X[:,0] = labelEncoder_X.fit_transform(X[:,0])
onehatencoder = OneHotEncoder(categorical_features=[0])
X = onehatencoder.fit_transform(X).toarray()
labelEncoder_Y = LabelEncoder()
Y = labelEncoder_Y.fit_transform(Y)

# Spliting the data set into training set and test set

from sklearn.cross_validation import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y, test_size=0.2, random_state=0)

# Feature Scaling

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
