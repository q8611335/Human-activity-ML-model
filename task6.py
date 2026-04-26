import json
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def task6():
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
    C_values = [0.01, 0.1, 1, 10, 100, 1000]
    train_accuracy = []
    test_accuracy = []

    # train and test based on different C value        
    for c in C_values:
        svm = SVC(kernel='linear', C=c, random_state=7)
        svm.fit(X_train, y_train)

        train_accuracy.append(svm.score(X_train, y_train))
        test_accuracy.append(svm.score(X_test,y_test))

    # create line plot
    plt.figure(figsize=(24, 8))
    plt.plot(C_values, train_accuracy, marker='o', label='Training accuracy')
    plt.plot(C_values, test_accuracy, marker='s', label='Test accuracy')
    plt.xscale('log')

    plt.title('task6_svm_accuracy')
    plt.xlabel('C values (log scale)')
    plt.ylabel('Accuracy')
    plt.xticks(C_values, label=C_values)
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.savefig('task6_svm_accuracy.png')

    return
