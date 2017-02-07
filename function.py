"""Functions"""

def connect(x):

    call()
    message()
    print "ccc"
    return x

def call ():
	print "call method is called"

def message ():
	print "message"

print connect(10)

#factorial
a=5
fact=1
for i in range(1,a+1):
    fact=fact*i         #1, 2,  6, 24, 120

print fact

#try this in recursive fuction
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print fact(5)


"""List to dictionary"""

#10*20
#20-30
#30-60
#>60
#ditcionary
li=[25,35,47,45,56,66,77,86,21,16,54,97]
#find second max value
#whoch group is having the max number of members in above list. try in dictionary

r1=[]
r2=[]
r3=[]
r4=[]
for age in li:
    if age>=10 and age<20:
       #print "range1"
       r1.append(age)

    elif age>=20 and age<30:
      # print "range2"
       r2.append(age)
    elif age>=30 and age<60:
      # print "range3"
       r3.append(age)
    else:
       # print "range4"
        r4.append(age)

print " R1 ",r1,"R2 ",r2,"R3 ",r3,"R4",r4

d={}
d['R1']=r1
d['R2']=r2
d['R3']=r3
d['R4']=r4
print "Dictionary with range of elements",d

"""
Finding average time spent on facebook

dict with key as person name and each key has value list. the list contains contain a tuple .tuple consists of login, logout

d={Nandi:[(12,3),()], Krishna:[]}

findout average login time in facebook

for 5 days each u spend 30-40 min
   function avg time
"""
from datetime import datetime,timedelta
#import datetime

d={'Nandi': [(datetime(2017, 2, 5, 11, 2), datetime(2017, 2, 5, 12, 2)),(datetime(2017, 2, 4, 10, 2), datetime(2017, 2, 4, 12, 2)),(datetime(2017, 2, 3, 10, 2),datetime(2017, 2, 4, 11, 2))],
   'krishna': [(datetime(2017, 2, 5, 8, 2),datetime(2017, 2, 5, 10, 12)),(datetime(2017, 2, 4, 11, 22),datetime(2017, 2, 4, 12, 22)),(datetime(2017, 2, 3, 9, 2),datetime(2017, 2, 4, 12, 22))]}
def avg(list_val):
    li=[]
    for row in val:
       #print row[0],row[1]
        diff=row[1]-row[0]
        #print diff
        li.append(diff.seconds)
    print li
    avg_time=sum(li)/len(li)
    print "Avg time for  3 days in minutes",avg_time/60


for key,val in d.items():
    #print key,val
    avg(val)



