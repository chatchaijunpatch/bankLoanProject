import re
import pandas as pd 
import numpy as np
from datetime import date, datetime 
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
import warnings
warnings.filterwarnings('ignore')

def dataSet():
    df =pd.read_csv('model Analysis/Default_Fin.csv')
    df = df.drop(['Index','Employed'],axis=1)
    return df
def train():
    df = dataSet()
    x=df.drop(['Defaulted?'],axis=1).values
    y = df['Defaulted?'].values.reshape(-1,1)
    model = KNeighborsClassifier(n_neighbors=3)
    return model.fit(x,y)


def accuracy():
    df = dataSet()
    x=df.drop(['Defaulted?'],axis=1).values
    y = df['Defaulted?'].values.reshape(-1,1)
    model = train()
    return accuracy_score(y,model.predict(x))


def prediction(data):
    model = train()
    return model.predict(data.reshape(1,-1))


def calculateAge(born):
    born = datetime.strptime(born,"%Y-%m-%d")
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def personalConfig(personal):
    if personal == 'มี':
        return 1
    else:
        return 0
def initial(request):
    income = request.form['income']
    balance = request.form['balance']
    income = ((float(income))*12)
    balance = (float(balance))*12
 

    data = np.array([balance,income])
    return data


