'''Given a string and we have to swap its adjacent characters(pairs).

Here, to swap adjacent characters of a given string - we have a condition, which is "string length must be EVEN i.e. string must contains even number of characters".

Input Format

Take a string from the user.
Constraints

String length should not exceed 1000.
Output Format

It should print the swapped string.
if string length is odd then print "Odd length."
Sample Input 0

Hello
Sample Output 0

Odd length.
Sample Input 1

help
Sample Output 1

ehpl
'''
#code:
s=input()
if len(s) % 2 != 0:
    print("Odd length.")
else:
    print(''.join([ s[x:x+2][::-1] for x in range(0, len(s), 2) ]))