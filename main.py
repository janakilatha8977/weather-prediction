from src.preprocess import load_and_clean_data
from src.train_model import train_model
from src.predict import make_predictions
from src.visualize import plot_results

# Step 1: Load data
df = load_and_clean_data("data/weather_data.csv")

# Step 2: Train model
model, X_test, y_test = train_model(df)

# Step 3: Predict
y_pred = make_predictions(model, X_test)

# Step 4: Visualize
plot_results(y_test, y_pred)

print("Predicted values:", y_pred)
print("Actual values:", list(y_test))
