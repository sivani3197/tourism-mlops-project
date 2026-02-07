import os
import argparse
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_data", type=str)
    parser.add_argument("--preprocessed_data", type=str)
    args = parser.parse_args()

    df = pd.read_csv(args.input_data)

    # Preprocessing: Filling missing values
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['TypeofContact'] = df['TypeofContact'].fillna(df['TypeofContact'].mode()[0])
    df['MonthlyIncome'] = df['MonthlyIncome'].fillna(df['MonthlyIncome'].median())
    
    # Removes unnecessary columns
    if 'CustomerID' in df.columns:
        df = df.drop(['CustomerID'], axis=1)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(['Unnamed: 0'], axis=1)

    # Saves to the output path provided by Azure
    os.makedirs(args.preprocessed_data, exist_ok=True)
    df.to_csv(os.path.join(args.preprocessed_data, "cleaned_tourism.csv"), index=False)
    print("Preprocessing finished.")

if __name__ == "__main__":
    main()
