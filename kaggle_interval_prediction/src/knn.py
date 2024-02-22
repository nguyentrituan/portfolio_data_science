import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor



data_path = './data/'

train_data = data_path + 'train.csv'
test_data = data_path + 'test.csv'
sample_sub = data_path + 'sample_submission.csv'
submission = data_path + 'submission.csv'

df_train  = pd.read_csv(train_data, index_col="id")
df_test = pd.read_csv(test_data, index_col="id")

X = df_train.drop(["DBWT"], axis=1)
y = df_train["DBWT"]

X_train, X_validation, y_train, y_validation   = train_test_split(X, y, test_size=0.50, random_state = 42)
X_test = df_test 

X_train = pd.get_dummies(X_train)
X_validation = pd.get_dummies(X_validation)
X_test = pd.get_dummies(X_test)


if __name__ == "__main__":
    model = KNeighborsRegressor(n_neighbors=4)
    model.fit(X_train, y_train)

    train_std = np.std(y_train)
    train_std

    y_pred = model.predict(X_test)
    X_test["pi_lower"] = y_pred -  1.8 * train_std
    X_test["pi_upper"] = y_pred +  1.8 * train_std

    res = X_test[["pi_lower","pi_upper"]]
    res.to_csv(submission)