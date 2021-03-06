# -*- coding: utf-8 -*-
"""HR.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsNay5ScAYr2MX57qYyRhUTqS2-8MnSc
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

import tensorflow as tf

hr= pd.read_csv("hr.csv")
hr.head()

np.unique(hr['Over18'])

np.unique(hr['OverTime'])

hr.info()

hr.describe()

hr['Attrition']= hr['Attrition'].apply(lambda x:1 if x == 'Yes' else 0)
hr['Over18']= hr['Over18'].apply(lambda x:1 if x == 'Y' else 0)
hr['OverTime']= hr['OverTime'].apply(lambda x:1 if x == 'Yes' else 0)
hr.head()

sns.heatmap(hr.isnull(), yticklabels= False, cbar= False, cmap= 'Blues')

hr.hist(bins= 20, figsize= (25, 25), color= 'r')

hr.drop(['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours' ], axis= 1, inplace= True)
hr.head()

left_emp= hr[hr['Attrition'] == 1]
stayed_emp= hr[hr['Attrition'] == 0]

print("No of emplyees left", len(left_emp))
print("%  of emplyees left", (len(left_emp)/len(hr))*100, '%')

print("No of emplyees stayed", len(stayed_emp))
print("%  of emplyees stayed", (len(stayed_emp)/len(hr))*100, '%')

left_emp.describe()

stayed_emp.describe()

"""Mean age of left employees is 33 and that of stayed employees is 37.

Avg daily rate of left employees is 750 and that of stayed employees is 812.

Avg distance from home of left employees is 10 km and that of stayed employees is 9 km.

Environment satisfaction of left employees is less than that of stayed employees.

Job Satisfaction of stayed employees is greater than that of left employees.

Work life balance of stayed employees is greater than that of left employees.
"""

correlations= hr.corr()
f, ax= plt.subplots(figsize= (20,20))
sns.heatmap(correlations, annot= True)

plt.figure(figsize= (25,12))
sns.countplot(x= 'Age', hue= 'Attrition', data= hr)

"""Many employees tend to leave the company from the age of 26-31."""

plt.figure(figsize= (20, 18))
plt.subplot(411)
sns.countplot(x= 'JobRole', hue= 'Attrition', data= hr)

plt.subplot(412)
sns.countplot(x= 'MaritalStatus', hue= 'Attrition', data= hr)

plt.subplot(413)
sns.countplot(x= 'JobInvolvement', hue= 'Attrition', data= hr)

plt.subplot(414)
sns.countplot(x= 'JobLevel', hue= 'Attrition', data= hr)

"""1. Job role
--> Most of the employees from sales representative role leave the company(around 44.44%).


2. Marital Status
--> Most of the single employees tend to leave the company(around 30%).


3. Job Involvement
--> Employees who have les job involvement tend to leave the company.


4. Job level
--> Employees who are freshers tend to leave the company.
"""

sns.kdeplot(left_emp['DistanceFromHome'], label= 'Left employees', shade= True, color='red')
sns.kdeplot(stayed_emp['DistanceFromHome'], label= 'Stayed employees', shade= True, color='blue')

plt.xlabel('Distance From home')

"""As the distance from home increases more employees tend to leave the company."""

sns.kdeplot(left_emp['YearsWithCurrManager'], label= 'Left employees', shade= True, color='red')
sns.kdeplot(stayed_emp['YearsWithCurrManager'], label= 'Stayed employees', shade= True, color='blue')

plt.xlabel('YearsWithCurrManager')

"""As the Years with Current Manager increase many employees tend to stay in the company."""

sns.kdeplot(left_emp['TotalWorkingYears'], label= 'Left employees', shade= True, color='red')
sns.kdeplot(stayed_emp['TotalWorkingYears'], label= 'Stayed employees', shade= True, color='blue')

plt.xlabel('TotalWorkingYears')

"""Many employees tend to leave the company at the starting of their career."""

sns.boxplot(x='Gender', y='MonthlyIncome', data= hr)

"""The average monthly income of females and males are almost same."""

plt.figure(figsize= (20, 7))
sns.boxplot(x='JobRole', y='MonthlyIncome', data= hr)

"""Managers and Research Directors have a high monthly income whereas Research Scientist and Laboratory Technician have low income."""

numerics= ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
cat= ['O']

x_cat= hr.select_dtypes(include= cat)

onehot= OneHotEncoder()
x_cat= onehot.fit_transform(x_cat).toarray()
x_cat= pd.DataFrame(x_cat)

x_numerical= hr.select_dtypes(include= numerics)
x_numerical

x_combined= pd.concat([x_numerical, x_cat], axis= 1)
x_combined

scaler= MinMaxScaler()
x= scaler.fit_transform(x_combined)
x

y= x_combined['Attrition']
y

X_train, X_test, y_train, y_test= train_test_split(x, y, test_size= 0.2)

model= LogisticRegression()
model.fit(X_train, y_train)
y_pred= model.predict(X_test)

print("Accuracy:", accuracy_score(y_pred, y_test))

cm= confusion_matrix(y_pred, y_test)
sns.heatmap(cm, annot= True, fmt= 'd')

print("Classification report:", classification_report(y_pred, y_test))

model= RandomForestClassifier()
model.fit(X_train, y_train)
y_pred= model.predict(X_test)

cm= confusion_matrix(y_pred, y_test)
sns.heatmap(cm, annot= True, fmt='d')



