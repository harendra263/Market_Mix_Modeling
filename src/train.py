import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from . import dispatcher


TRAINING_DATA = os.environ.get("TRAINING_DATA")
MODEL = os.environ.get("MODEL")

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA, usecols= lambda x: x != "Unnamed: 0")

    X = df.drop('sales', axis=1)
    y = df.sales

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    reg = dispatcher.MODELS[MODEL]
    reg.fit(X_train, y_train)
    pred = reg.predict(X_test)

    feat_importance = pd.Series(data=reg.feature_importances_, index=X.columns)
    print(feat_importance.head)