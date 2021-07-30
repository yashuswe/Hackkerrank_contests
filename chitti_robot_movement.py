'''Consider a robot in the position (0, 0). The robot can move in all the four directions i.e left, right, up and down. With the given robot moves print whether the robot moved in a circle or not.

Input Format

First line will contain a String pattern ie Moves of Robot

Constraints

pattern can contain only L R U D (Characters String)

Output Format

Second line will print a boolean value

Sample Input 0

LR
Sample Output 0

true
Sample Input 1

UU
Sample Output 1

false
'''
#code:
s=input()
l=0
u=0
d=0
r=0
for i in s:
    if i == 'U':
        u=u+1
    elif i == 'R':
        r=r+1
    elif i == 'D':
        d=d+1
    elif i == 'L':
        l=l+1
if (l==r and u==d):
    print("true")
else:
    print("false")