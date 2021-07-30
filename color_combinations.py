'''We have three colors: red, green, and blue in a list. 
Replace the two different colors pair with third color in every dutye cycle of transformation. 

Given N colors are in a line, determine the last remaining color after any possible sequence of such transformations.

For example, given the list is ['R', 'G', 'B', 'R'] 
and the following steps we need to take in transformation.
image

("R", "G")  ---> "B"
("B", "G")  ---> "R"
("B", "R")  ---> "G"
Input Format

list of colors

Constraints

None

Output Format

Color

Sample Input 0

["R", "G", "B", "R", "G"]
Sample Output 0

"B"
Explanation 0

['R', 'G', 'B', 'R', 'G']
{'G', 'R'}---> {'B'} ['B', 'B', 'R', 'G']
{'R', 'B'}---> {'G'} ['B', 'G', 'G']
{'G', 'B'}---> {'R'} ['R', 'G']
{'G', 'R'}---> {'B'} ['B']
Output representation : "B"
Sample Input 1

["R", "G", "B", "R", "G", "R", "B"]
Sample Output 1

"R"
Explanation 1

['R', 'G', 'B', 'R', 'G', 'R', 'B']
{'G', 'R'}---> {'B'} ['B', 'B', 'R', 'G', 'R', 'B']
{'R', 'B'}---> {'G'} ['B', 'G', 'G', 'R', 'B']
{'G', 'B'}---> {'R'} ['R', 'G', 'R', 'B']
{'G', 'R'}---> {'B'} ['B', 'R', 'B']
{'R', 'B'}---> {'G'} ['G', 'B']
{'G', 'B'}---> {'R'} ['R']
'''
#code by yashassvi:
s = input()
lst = []
for i in s:
    if i.isalpha():
        lst.append(i)
while(len(lst)!=1):
    n=1
    while(len(lst)>len(lst)-1):
        if lst[n] == 'G' and lst[n-1] == 'B':
                lst[n] = 'R'
                lst.pop(n-1)
                break
        elif lst[n] == 'G' and lst[n-1] == 'R':
                lst[n] = 'B'
                lst.pop(n-1)
                break
        elif lst[n] == 'R' and lst[n-1] == 'G':
                lst[n] = 'B'
                lst.pop(i-1)
                break
        elif lst[n] == 'R' and lst[n-1] == 'B':
                lst[n] = 'G'
                lst.pop(n-1)
                break
        elif lst[n] == 'B' and lst[n-1] == 'G':
                lst[n] = 'R'
                lst.pop(n-1)
                break
        elif lst[n] == 'B' and lst[n-1] == 'R':
                lst[n] = 'G'
                lst.pop(n-1)
                break
        else:
            n += 1
print('"',end="")
print(*lst,end="")
print('"')