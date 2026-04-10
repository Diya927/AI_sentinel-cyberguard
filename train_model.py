import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib

from src.data_preprocessing import load_data, preprocess_data

# Load data
df = load_data("data/KDDTrain+.txt")
df = preprocess_data(df)

# -------------------------
# ENCODE CATEGORICAL COLUMNS
# -------------------------
cat_cols = ["protocol_type", "service", "flag"]

encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# -------------------------
# SPLIT DATA
# -------------------------
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# TRAIN MODEL
# -------------------------
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------------
# EVALUATE
# -------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# -------------------------
# SAVE MODEL
# -------------------------
joblib.dump(model, "cyber_model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("Model saved successfully")