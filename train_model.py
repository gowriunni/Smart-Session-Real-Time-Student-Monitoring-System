import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

#LOADING THE TRAINING DATA
print("📥 Loading training data...")
data = pd.read_csv("training_data.csv")
print("Data loaded successfully")

#DISPLAY FIRST FEW ROWS
print(data.head()) 

#SEPERATING FEATURES AND LABLES
features = data[[
    "brow_distance",
    "mouth_opening",
    "head_tilt",
    "gaze"
]]

labels = data["label"]

#ENCODING TEXT LABELS INTO NUMBERS
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels)

#SPLITTING DATA 
X_train, X_test, y_train, y_test = train_test_split(
    features,
    labels_encoded,
    test_size=0.2,
    random_state=42
)

#CREATING THE MACHINE LEARNING MODEL
model = RandomForestClassifier(
    n_estimators=100,  
    random_state=42
)

#TRAINING THE MODEL
model.fit(X_train, y_train)

#SAVING THE MODEL
joblib.dump(model, "behavior_model.pkl")
joblib.dump(label_encoder, "label_encoder.pkl")

print("✅ Model trained successfully")
print("📁 Files saved:")
print(" - behavior_model.pkl")
print(" - label_encoder.pkl")

#CHECKING ACCURACY
accuracy = model.score(X_test, y_test)
print(f"🎯 Model Accuracy: {accuracy * 100:.2f}%")
