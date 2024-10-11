import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import mlflow


def train_val_loss_plot(run_id, plot=False):
    train_history = mlflow.tracking.MlflowClient().get_metric_history(run_id=run_id, key="train_loss")
    validation_history = mlflow.tracking.MlflowClient().get_metric_history(run_id=run_id, key="validation_loss")

    fig = plt.figure()
    plt.plot([m.step for m in train_history], [m.value for m in train_history], label="Train Loss")
    plt.plot([m.step for m in validation_history], [m.value for m in validation_history], label="Validation Loss")
    plt.title("Train - Validation Loss Curves")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show() if plot else plt.close()
    
    return fig


def confusion_matrix_plot(y_true, y_pred, classes=None, figsize=(10, 10), text_size=15):
    cm = confusion_matrix(y_true, y_pred)
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]
    n_classes = cm.shape[0]

    fig, ax = plt.subplots(figsize=figsize)
    cax = ax.matshow(cm, cmap=plt.cm.Blues)
    fig.colorbar(cax)

    labels = classes if classes else np.arange(cm.shape[0])

    ax.set(title="Confusion Matrix", xlabel="Predicted label",  ylabel="True label", 
           xticks=np.arange(n_classes), yticks=np.arange(n_classes), xticklabels=labels, yticklabels=labels)

    ax.xaxis.set_label_position("bottom")
    ax.xaxis.tick_bottom()

    threshold = (cm.max() + cm.min()) / 2.

    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, f"{cm[i, j]} ({cm_norm[i, j]*100:.1f}%)",
                 horizontalalignment="center",
                 color="white" if cm[i, j] > threshold else "black",
                 size=text_size)