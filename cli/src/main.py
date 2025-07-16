import pandas as pd
import matplotlib.pyplot as plt
import os

# Column names for the dataset
col_names = [
    'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
    'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'
]

def main():
    path = './data/heart_cleveland.csv'
# './data/.heart_cleverland.csv'

    # Check if file exists
    if not os.path.exists(path):
        print(f"X file not found at {path}")
        return

    # Load the dataset
    df = pd.read_csv(path, names=col_names)
    print('Data loaded successfully!')
    print(df.head())

    # Generate age distribution chart
    charts_dir = './charts'
    os.makedirs(charts_dir, exist_ok=True)

    plt.figure(figsize=(8, 5))
    df['age'].hist(bins=10, color='skyblue', edgecolor='black')
    plt.title('Age Distribution of Heart Patients')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.tight_layout()

    chart_path = os.path.join(charts_dir, 'age_distribution.png')
    plt.savefig(chart_path)
    print(f"Chart saved at {chart_path}")

if __name__ == '__main__':
    main()
