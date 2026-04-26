import pandas as pd
import json
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.metrics import confusion_matrix, classification_report

def task4():
    df = pd.read_csv("HumanActivityRecognition_Scaled.csv")
    y = df['Activity']
    X = df.drop(columns=['Activity', 'subject'])

    # data split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        train_size=0.8,
        random_state=7,
        shuffle=True,
        stratify=y
    )
    # train GaussianNB model
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    accuracy_gnb = gnb.score(X_test, y_test)
    accuracy_gnb_round = round(accuracy_gnb, 2)

    # train KNN model
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    accuracy_knn = knn.score(X_test, y_test)
    accuracy_knn_round = round(accuracy_knn, 2)

    # create output dic and save as json
    output_gnb = {
        "The accuracy of GaussianNB (scaled data)": accuracy_gnb_round
    }
    with open("task4_gnb_accuracy.json", "w") as t4:
        json.dump(output_gnb, t4, indent=4)

    output_knn = {
        "The accuracy of KNN (scaled data)": accuracy_knn_round
    }
    with open("task4_knn_accuracy.json", "w") as t4knn:
        json.dump(output_knn, t4knn, indent=4)
    
    # get prediction result
    y_pred = gnb.predict(X_test)

    # create confusion matrix 
    cm = confusion_matrix(y_test, y_pred) 
    classes = sorted(y_test.unique())
    plt.figure(figsize=(24, 8))
    sb.heatmap(
        cm,
        annot=True,
        fmt='d',
        cmap='Blues',
        xticklabels=classes,
        yticklabels=classes
    )
    plt.title('task4_gnb_heatmap')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.savefig('task4_gnb_heatmap.png')
    plt.close()

    # calculate precision, recall, f1-score
    report = classification_report(
        y_test, y_pred,
        target_names=classes,
        output_dict=True
    )
    # create output dic and save as json
    performance_report = {}
    for class_name in classes:
        performance_report[class_name] = {
            "precision": report[class_name]['precision'],
            "recall": report[class_name]['recall'],
            "f1-score": report[class_name]['f1-score']
        }
    with open("task4_gnb_performance.json", "w") as t4report:
        json.dump(performance_report, t4report, indent=4)
    return
