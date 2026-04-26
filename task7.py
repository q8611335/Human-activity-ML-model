import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
def task7():
    # read and split data
    df = pd.read_csv("HumanActivityRecognition_Scaled.csv")
    y = df['Activity']
    X = df.drop(columns=['Activity', 'subject'])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        train_size=0.8,
        random_state=7,
        shuffle=True,
        stratify=y
    )    

    # train logistic regression model
    lr = LogisticRegression(random_state=7)
    lr.fit(X_train, y_train)

    # calculate accuracy
    train_accuracy = lr.score(X_train, y_train)
    test_accuracy = lr.score(X_test, y_test)
    
    # get coefficient matrix from training model
    coefficient_matrix = lr.coef_
    feature_names = X.columns.tolist()

    # calculate the average absolute importance for each feature
    avg_importance = np.mean(np.abs(coefficient_matrix), axis=0)
    
    # sort index by importance value in descending order and slice the first 5 to get top 5
    top_5_index = np.argsort(avg_importance)[::-1][:5]
    top_5_feature = {}
    for i in top_5_index:
        top_5_feature[feature_names[i]] = avg_importance[i]

    # create output dic and save as json
    output = {
        "training_accuracy": train_accuracy,
        "test_accuracy": test_accuracy,
        "coefficient_matrix_shape": list(coefficient_matrix.shape),
        "first_5_feature_names": feature_names[:5],
        "top_5_features": top_5_feature
    }
    
    with open("task7_logistic_regression.json", "w") as t7:
        json.dump(output, t7, indent=4)
    return
