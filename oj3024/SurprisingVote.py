"""SurprisingVote"""

all_ = float(input())
highest = float(input())

thi = all_ - highest * 2

if thi <=0:
    thi = 0
if highest - thi > 2:
    print("Surprising")
else:
    print("Not surprising")
