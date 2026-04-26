import pandas as pd
import json

def task1():

    # load dataset
    df = pd.read_csv("HumanActivityRecognition_Unscaled.csv")
    # count rows and columns
    row = len(df)
    col = len(df.columns)
    # count class
    class_counts = {
        "WALKING": int((df["Activity"] == "WALKING").sum()),
        "WALKING_UPSTAIRS": int((df["Activity"] == "WALKING_UPSTAIRS").sum()),
        "WALKING_DOWNSTAIRS": int((df["Activity"] == "WALKING_DOWNSTAIRS").sum()),
        "SITTING": int((df["Activity"] == "SITTING").sum()),
        "STANDING": int((df["Activity"] == "STANDING").sum()),
        "LAYING": int((df["Activity"] == "LAYING").sum()),
    }
    # create output dict
    output = {
        "Total number of rows" : row,
        "Total number of columns" : col,
        "Class counts" : class_counts
    }

    # save as json
    with open("task1_statistics.json", "w") as t1:
        json.dump(output, t1, indent=4)
    return output
