import numpy as np
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt


def MSE(y_test, y_pred):
    return np.sum(np.square(y_pred - y_test)) / y_pred.shape[0]

def r2_score(y_test, y_pred):
    # Test set label mean
    y_avg = np.mean(y_test)
    # Sum of squares of total dispersion
    ss_tot = np.sum((y_test - y_avg) ** 2)
    # Sum of squares of residuals
    ss_res = np.sum((y_test - y_pred) ** 2)
    # R calculation
    r2 = 1 - (ss_res / ss_tot)
    return r2

def MAE(y_test, y_pred):
    return np.sum(abs(y_pred - y_test)) / y_pred.shape[0]


def RMSE(y_test, y_pred):
    return pow(np.sum(np.square(y_pred - y_test)) / y_pred.shape[0], 0.5)


def confusion_matrix(true_labels, predicted_labels):
    unique_classes = np.unique(np.concatenate((true_labels, predicted_labels)))
    num_classes = len(unique_classes)
    confusion = np.zeros((num_classes, num_classes), dtype=int)
    for i in range(len(true_labels)):
        true_class = int(true_labels[i])
        predicted_class = int(predicted_labels[i])
        confusion[true_class][predicted_class] += 1
    plot_matrix(confusion)
    return confusion

def plot_matrix(matrix):
    df_cm = pd.DataFrame(matrix, range(len(matrix)), range(len(matrix)))
    # plt.figure(figsize=(10,7))
    sn.set(font_scale=1.4) # for label size
    sn.heatmap(df_cm, annot=True, annot_kws={"size": 16}) # font size
    plt.show()