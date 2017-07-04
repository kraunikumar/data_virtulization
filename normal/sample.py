from scipy.stats import norm
import statistics 
n=[]
print "this is calculated by taking raw data so please enter number of people visiting to the store per hour for 12 hrs"  
for i in range(0,11):

     print "In ", i+1, "hour"
     m=raw_input("enter number of people ")

    
     n.append(m)
print n
#entered values are in string format so they need to be coonver to int format
n=[int(x) for x in n]

#utilised mean and sd from statistics module 
mean = statistics.mean(n)
sd = statistics.stdev(n)
print "value of mean is",mean
print "value of sd is",sd

o=raw_input(" enter the value of x to compute normal distribution :")
o=int(o)
g=norm(mean, sd).pdf(o)
print "probability at ", o ," would be", g
