import statistics as st
import math
import pandas as pd
df=pd.read_csv('C:/Users/khada/Downloads/python/c105/class1.csv')
marks=df['Marks'].tolist()
n= len(marks)
mean=st.mean(marks)
sum=0
for m in marks:
    s=m-mean
    sq=s*s
    sum=sum+sq
result=sum/(n-1)
std=math.sqrt(result)
print(std)
