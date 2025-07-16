import pandas as pd

col_names = [
    'age','sex','cp','trestbps','chol','fbs','restecg',
    'thalach','exang','oldpeak','slope','ca','thal','target'
            ]

def main():
   path = '../data/heart_cleveland.csv'
   df = pd.read_csv(path,names=col_names)

   print('Data loaed successfully!')
   print(df.head())

if __name__ == '__main__':
       main() 
    