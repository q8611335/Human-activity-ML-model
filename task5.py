import json
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def task5():
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
    
    # train decision tree model
    dt = DecisionTreeClassifier(criterion='entropy', random_state=7)
    dt.fit(X_train, y_train)

    # calculate accuracy, depth and root
    accuracy_dt = dt.score(X_test, y_test)
    tree_depth = dt.get_depth()
    root_index = dt.tree_.feature[0]
    root_name = X.columns[root_index]

    # create output dic and save as json
    output = {
       "The accuracy of Decision Tree (default max_depth)": accuracy_dt,
        "The depth of trained Decision Tree": tree_depth,
        "The feature at the root of the tree": root_name
    }
    with open("task5_dt_statistics.json", "w") as t5:
        json.dump(output, t5, indent=4)
    
    # visualise first 3 levels
    plt.figure(figsize=(20, 10))
    plot_tree(
        dt,
        max_depth=2,
        feature_names=X.columns.tolist(),
        class_names=sorted(y.unique()),
        filled=True,
        fontsize=8
    )
    plt.title("task5_dt_visualisation")
    plt.savefig('task5_dt_visualisation.png')
    return
