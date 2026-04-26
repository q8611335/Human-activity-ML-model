import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import json

def task3():
    # load data
    df = pd.read_csv("HumanActivityRecognition_Unscaled.csv")
    # set target label as y
    y = df['Activity']
    # set all other features as x
    X = df.drop(columns=['Activity', 'subject'])
    
    # data split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        train_size=0.8,
        random_state=7,
        stratify=y,
        shuffle=True
    )

    # train KNN model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    # test accuracy and round up
    accuracy = knn.score(X_test, y_test)
    accuracy_round = round(accuracy, 2)

    # creat output dic and save as json
    output = {
        "The accuracy of KNN (unscaled data)": accuracy_round
    }
    with open("task3_unscaled_knn_accuracy.json", "w") as t3:
        json.dump(output, t3, indent=4)
    
    # initialise scaler
    scaler = StandardScaler()
    # standardise and transform the train data
    X_train_scaled = scaler.fit_transform(X_train)
    # transform the test data
    X_test_scaled = scaler.transform(X_test)

    # train new KNN model with scaled data
    knn_scaled = KNeighborsClassifier(n_neighbors=5)
    knn_scaled.fit(X_train_scaled, y_train)
    accuracy_scaled = knn_scaled.score(X_test_scaled, y_test)
    accuracy_scaled_round = round(accuracy_scaled, 2)
    
    #create scaled output as json
    output_scaled = {
        "The accuracy of KNN (scaled data)": accuracy_scaled_round
    }
    with open("task3_scaled_knn_accuracy.json", "w") as t3scaled:
        json.dump(output_scaled, t3scaled, indent=4)

    return
