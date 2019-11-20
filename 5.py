import pandas as pd
import numpy as np

dataset = pd.read_csv('pima-indians-diabetes.data.csv')

dataset.columns = [
    "NumTimesPrg", "PlGlcConc", "BloodP",
    "SkinThick", "TwoHourSerIns", "BMI",
    "DiPedFunc", "Age", "HasDiabetes"]

dataset.shape

#1st output so press enter

corr = dataset.corr()



median_bmi = dataset['BMI'].median()
dataset['BMI'] = dataset['BMI'].replace(
    to_replace=0, value=median_bmi)


median_bloodp = dataset['BloodP'].median()

dataset['BloodP'] = dataset['BloodP'].replace(
    to_replace=0, value=median_bloodp)


median_plglcconc = dataset['PlGlcConc'].median()

dataset['PlGlcConc'] = dataset['PlGlcConc'].replace(
    to_replace=0, value=median_plglcconc)

median_skinthick = dataset['SkinThick'].median()
dataset['SkinThick'] = dataset['SkinThick'].replace(
    to_replace=0, value=median_skinthick)


median_twohourserins = dataset['TwoHourSerIns'].median()

dataset['TwoHourSerIns'] = dataset['TwoHourSerIns'].replace(
    to_replace=0, value=median_twohourserins)

from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(
    dataset, test_size=0.2, random_state=42)


train_set_labels = train_set["HasDiabetes"].copy()
train_set = train_set.drop("HasDiabetes", axis=1)

test_set_labels = test_set["HasDiabetes"].copy()
test_set = test_set.drop("HasDiabetes", axis=1)


from sklearn.preprocessing import MinMaxScaler as Scaler

scaler = Scaler()
scaler.fit(train_set)
train_set_scaled = scaler.transform(train_set)
test_set_scaled = scaler.transform(test_set)

from sklearn.naive_bayes import GaussianNB

X = train_set_scaled
Y = train_set_labels

clf =GaussianNB()

    
clf.fit(X,Y)

pred = clf.predict(test_set) 


from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred,test_set_labels) 
print( accuracy)
