import statsmodels.formula.api as sm
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("input/Advertising.csv", usecols= lambda x: x != "Unnamed: 0")

    model = sm.ols(formula="sales ~ TV+radio+newspaper", data=df).fit()

    print(model.summary())

    y_pred = model.predict()
    labels = df['sales']
    df_temp = pd.DataFrame({"Actuals": labels, "Predicted": y_pred})
    df_temp.head()
    
    