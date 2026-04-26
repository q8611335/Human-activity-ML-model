import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def task2():
    # load dataset
    df = pd.read_csv("HumanActivityRecognition_Unscaled.csv")
    # define plot features
    features = [
        'tGravityAcc-mean()-X', 
        'tBodyAcc-mean()-X',
        'fBodyAcc-mean()-X'
    ]

    # build 1 row 3 cols plot
    fig, axes = plt.subplots(1, 3, figsize=(24, 8))

    #iterate all features in csv
    for i, feature in enumerate(features):
        sb.violinplot(ax=axes[i], x='Activity', y=feature, data=df, hue='Activity')

        axes[i].set_title(f'Distribution of {feature}')
        axes[i].tick_params(axis='x', rotation=45)

    plt.tight_layout()

    # save as png
    plt.savefig("task2_discriminative_power.png")

    return
