import matplotlib.pyplot as plt

def plot_results(y_test, y_pred):
    plt.scatter(y_test, y_pred, color='blue')
    plt.xlabel("Actual Temperature")
    plt.ylabel("Predicted Temperature")
    plt.title("Weather Prediction")
    plt.show()
