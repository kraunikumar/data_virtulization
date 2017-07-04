import math 
import csv

mean=input("enter mean  value")

k=[]
for x in range(0,10):
    p=(mean**x)*math.exp(-mean)/math.factorial(x)
    k.append(p)

with open('output.csv','w')as f:
    writer=csv.writer(f)
    data=[[1,k[0]],[2,k[2]],[3,k[3]]]
    for row in data: 
      writer.writerows([row])
f.close()



