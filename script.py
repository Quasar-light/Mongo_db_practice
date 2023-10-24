import pandas as pd

df = pd.read_csv('/Users/kali/Documents/GitHub/Mongo_db_practice/student/student-mat.csv', delimiter=';')
df.paid =[1 if x == "yes" else 0 for x in df.paid]