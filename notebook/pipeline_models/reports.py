from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_classification_report(y_test, y_pred):

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    return accuracy, report, cm

def plot_confusion_matrix(cm, model):
    plt.figure(figsize=(8,6))
    sns.heatmap(cm, annot=True, cmap='Blues')
    plt.xlabel("Predicted label")
    plt.ylabel("Actual label")
    plt.title(f"Confusion Matrix - {model}")
    plt.show()
