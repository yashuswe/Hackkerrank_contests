'''Given an array of names of winner condidates in an badminton matches series.
The candidate name in array represents a number of matches won in the event.
Print the name of candidates who won the max matches .
If there is tie, print lexicographically smaller name.'''
#Code
a=input().split(',')
b=""
c=0
d=0
for x in a:
    for y in a:
        if (x == y):
            c=c+1
    if (c>d):
        b=x
        d=c
    c=0
print(b)
