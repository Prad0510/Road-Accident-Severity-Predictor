import pickle
import pandas as pd

# Load trained model and feature names
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('feature_info.pkl', 'rb') as f:
    feature_info = pickle.load(f)
feature_names = feature_info['features']

# Get importances
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False)

# Save to CSV for reference and dashboard use
feature_importance.to_csv('feature_importance.csv', index=False)

print(feature_importance.head(10))
