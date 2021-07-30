'''Given an array of integers, find the maximum AND(bitwise) of any two elements.

Input Format

space separated integers elements

Constraints

len(array)>0

Output Format

integer number

Sample Input 0

90 43 11 4 20
Sample Output 0

16'''
#code:
l=list(map(int,input().split(' ')))
n=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if((l[i] & l[j]) > n):
            n=(l[i] & l[j])
print(n)