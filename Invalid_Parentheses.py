#Invalid Parentheses
#An expression will be given which can contain open and close parentheses ,
#No other operator will be there in string. Find the paranthesis patterns is valid or not
#code by yashassvi:
n=input()
c=0
for i in n:
    if i == '(':
        c += 1
    elif i == ')':
        c -= 1
        if c < 0:
            break
if c == 0:
    print("'True'")
else:
    print("'False'")     
