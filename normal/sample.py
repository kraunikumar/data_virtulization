import scipy.stats
import statistics as stat
n=[]
for i in range(0,7):


    m=raw_input("enter the value :")
    n.append(m)
print n
n=[int(x) for x in n]
mean = stat.mean(n)
sd = stat.stdev(n)
print mean
print sd

scipy.stats.norm(mean, sd).pdf(23)

