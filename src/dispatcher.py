from sklearn import ensemble

MODELS = {
    'randomforest': ensemble.RandomForestRegressor(n_estimators=100, n_jobs=-1, random_state=142),
    "extratrees": ensemble.ExtraTreesRegressor(n_estimators=100, n_jobs=-1, random_state=142)
}