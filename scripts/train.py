import os
import argparse
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prepared_data", type=str)
    args = parser.parse_args()

    # Load the cleaned data from the previous step
    df = pd.read_csv(os.path.join(args.prepared_data, "cleaned_tourism.csv"))

    # Encode categorical text into numbers
    le = LabelEncoder()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = le.fit_transform(df[col])

    # Features (X) and Target (y)
    X = df.drop(['ProdTaken'], axis=1)
    y = df['ProdTaken']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Start tracking the experiment in Azure ML
    with mlflow.start_run():
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)

        # Log accuracy metric
        acc = accuracy_score(y_test, model.predict(X_test))
        mlflow.log_metric("accuracy", acc)
        
        # Register the model in the Azure Model Registry
        mlflow.sklearn.log_model(model, "model", registered_model_name="tourism_wellness_model")
        print(f"Model trained with accuracy: {acc}")

if __name__ == "__main__":
    main()
