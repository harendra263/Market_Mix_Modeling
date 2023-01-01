## Marketing Mix Modelling
A Marketing Mix Model is a modeling technique used to determine market attribution, the estimated impact of each marketing channel that a given company is using.

Unlike Attribution Modeling, another technique used for marketing attribution, Marketing Mix Models attempt to measure the impact of immeasurable marketing channels, like TV, radio, and newspapers.

Generally, your output variable will be sales or conversions, but can also be things like website traffic. Your input variables typically consist of marketing spend by channel by period (day, week, month, quarter, etc…), but can also include other variables which we’ll get to later.

## Analysis

### 1. Looking for Trend wrt columns
![Trends]("/images/Trends.png")

### 2. Correlation Plot
![correlation]("/images/correlation.png")

### 3. Feature Importance
![Feature_Importance]("/images/Feature_Importance.png")


### 4. OLS MODEL
It’s time to build our marketing mix model! Another way to refer to the model we’re building is an OLS model, short for ordinary least squares, which is a method used to estimate the parameters in a linear regression model. An OLS model is a type of regression model that is most commonly used when building marketing mix models.

![OLS]("images/OLS/png")

1. .summary() provides us with an abundance of insights on our model. Going back to the output from .summary(), we can see a few areas to focus in on (you can reference these insights against the OLS regression results below):

2. The Adj. R-squared is 0.896. This means that approximately 90% of the total variation in the data can be explained by the model. This also means that the model doesn’t account for 10% of the data used — this could be due to missing variables, for example if there was another marketing channel that wasn’t included, or simply due to noise in the data.

3. At the top half, you can see Prob (F-statistic): 1.58e-96. This probability value (p-value) represents the likelihood that there are no good predictors of the target variable — in this case, there are no good predictors of sales. Since the p-value is close to zero, we know that there is at least one predictor in the model that is a good predictor of sales.

If you look at the column, P>|t|, you can see the p-values for each predictor. The p-values for TV and radio are less than 0.000, but the p-value for newspapers is 0.86, which indicates that newspaper spend has no significant impact on sales. Generally, you want the p-value to be less than 1% or 5%, which are the two standards in practice.